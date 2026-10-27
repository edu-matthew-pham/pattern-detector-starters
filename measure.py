"""
Measuring tools for the rules starters (colour_rules.py, sound_rules.py).

These functions only MEASURE things: what share of a photo is each colour, how loud a sound
is, what note it is. Deciding what the measurements mean is your job, in the rules you write.
You don't need to edit this file, but have a look inside.

Needs only numpy and Pillow.
"""
import math

import numpy as np
from PIL import Image, ImageOps

# ------------------------------------------------------------------ colours

MAX_SIDE = 400   # photos are shrunk to this size first, so measuring is quick


def _hsv(image):
    """A photo as three arrays: hue (0-360 degrees), saturation (0-100%) and brightness (0-100%)."""
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    image = ImageOps.exif_transpose(image)
    if image.mode in ("RGBA", "LA", "P"):
        image = image.convert("RGBA")
        white = Image.new("RGBA", image.size, (255, 255, 255, 255))
        image = Image.alpha_composite(white, image)
    image = image.convert("RGB")
    image.thumbnail((MAX_SIDE, MAX_SIDE))
    hsv = np.asarray(image.convert("HSV"), dtype=float)
    return image, hsv[..., 0] * 360 / 255, hsv[..., 1] * 100 / 255, hsv[..., 2] * 100 / 255


def colour_shares(image, colours, min_saturation=25, min_brightness=20, ignore_white=True):
    """What share (0 to 1) of the photo is each of your colours.

    colours: {"name": (hue_from, hue_to), ...} in degrees on the colour wheel:
             red 0, orange 30, yellow 60, green 120, cyan 180, blue 240, purple 280, back to red at 360.
             A range can wrap round: (340, 20) means reds either side of 0.
             Use the hue "dark" for pixels darker than min_brightness (e.g. brown spots, shadows).
    Pixels too grey (less colourful than min_saturation) don't count as any colour, and with
    ignore_white=True nor do white or very light pixels, so a plain background is left out.

    Returns (shares, preview): shares is {"name": share of the counted pixels}, and preview is a
    picture where each counted pixel is painted in its colour, so you can SEE what was measured.
    """
    rgb, h, s, v = _hsv(image)
    background = (v > 90) & (s < 15) if ignore_white else np.zeros_like(v, bool)
    colourful = (s >= min_saturation) & (v >= min_brightness)
    dark = (v < min_brightness) & ~background
    masks = {}
    for name, rng in colours.items():
        if rng == "dark":
            masks[name] = dark
            continue
        lo, hi = rng
        in_range = (h >= lo) & (h < hi) if lo <= hi else (h >= lo) | (h < hi)
        masks[name] = in_range & colourful
    counted = ~background
    total = max(int(counted.sum()), 1)
    shares = {name: float((m & counted).sum()) / total for name, m in masks.items()}

    preview = np.full(v.shape + (3,), 235, np.uint8)               # light grey: not counted
    preview[background] = 255                                      # white: background
    pixels = np.asarray(rgb)
    for m in masks.values():
        preview[m] = pixels[m]
    return shares, Image.fromarray(preview)


def brightness(image):
    """Average brightness of the photo, 0 (black) to 100 (white)."""
    return float(_hsv(image)[3].mean())


# ------------------------------------------------------------------ sounds

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def to_samples(sound):
    """Gradio's (rate, samples) or a .wav path -> (rate, mono float samples from -1 to 1)."""
    if isinstance(sound, str):
        import wave
        with wave.open(sound) as w:
            rate, width, channels = w.getframerate(), w.getsampwidth(), w.getnchannels()
            raw = w.readframes(w.getnframes())
        kind = {1: np.uint8, 2: np.int16, 4: np.int32}[width]
        samples = np.frombuffer(raw, kind).reshape(-1, channels)
        sound = (rate, samples)
    rate, samples = sound
    x = np.asarray(samples)
    if x.ndim > 1:
        x = x.astype(np.float64).mean(axis=1) if x.dtype.kind == "f" else x.mean(axis=1).astype(x.dtype)
    if x.dtype == np.uint8:
        x = (x.astype(np.float64) - 128) / 128
    elif x.dtype.kind == "i":
        x = x.astype(np.float64) / (2 ** (8 * x.dtype.itemsize - 1))
    return int(rate), x.astype(np.float64)


def loudness(samples):
    """How loud, in decibels below the loudest possible sound: 0 is the maximum, -20 is loud,
    -40 is quiet, -60 and below is near silence."""
    rms = math.sqrt(float(np.mean(np.square(samples)))) if len(samples) else 0.0
    return 20 * math.log10(rms) if rms > 1e-6 else -120.0


def loudest_part(rate, samples, seconds=0.5):
    """The loudest stretch of the recording (where the note is clearest)."""
    n = int(rate * seconds)
    if len(samples) <= n:
        return samples
    energy = np.convolve(np.square(samples), np.ones(n), mode="valid")
    start = int(np.argmax(energy))
    return samples[start:start + n]


def pitch(rate, samples, lowest=60, highest=1500):
    """The main pitch in Hz (how many vibrations per second), or None if there's no clear note.

    It looks for the time gap after which the sound repeats itself best (autocorrelation).
    """
    x = samples - np.mean(samples)
    if len(x) < rate / lowest * 2 or loudness(x) < -50:
        return None
    size = 1 << (2 * len(x) - 1).bit_length()
    spectrum = np.fft.rfft(x, size)
    ac = np.fft.irfft(spectrum * np.conj(spectrum))[:len(x)]
    ac /= ac[0]
    lo, hi = int(rate / highest), int(rate / lowest)
    seg = ac[lo:hi]
    if not len(seg):
        return None
    best = int(np.argmax(seg))
    if seg[best] < 0.5:                          # doesn't repeat clearly: noise, not a note
        return None
    # the earliest peak nearly as strong as the best avoids landing an octave too low
    peaks = [i for i in range(1, len(seg) - 1) if seg[i] >= seg[i - 1] and seg[i] >= seg[i + 1] and seg[i] > 0.9 * seg[best]]
    k = peaks[0] if peaks else best
    if 0 < k < len(seg) - 1:                     # fine-tune between samples
        a, b, c = seg[k - 1], seg[k], seg[k + 1]
        k = k + 0.5 * (a - c) / (a - 2 * b + c) if (a - 2 * b + c) else k
    return rate / (lo + k)


def note_of(hz):
    """Hz -> (note name like "A4", cents off: + is sharp/too high, - is flat/too low).
    100 cents is one semitone (one piano key)."""
    midi = 69 + 12 * math.log2(hz / 440)
    nearest = round(midi)
    return f"{NOTE_NAMES[nearest % 12]}{nearest // 12 - 1}", round((midi - nearest) * 100)


def cents_off(hz, target_note):
    """How far hz is from a target note like "A4", in cents (+ sharp, - flat)."""
    return round(1200 * math.log2(hz / frequency_of(target_note)))


def frequency_of(note):
    """"A4" -> 440.0 Hz."""
    name, octave = note[:-1], int(note[-1])
    return 440 * 2 ** ((NOTE_NAMES.index(name) + 12 * (octave + 1) - 69) / 12)
