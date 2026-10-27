# ------------------------------------------------------------------
# SOUND RULES: a note checker
# Measures how loud a sound is and which note it is, then YOUR rules
# decide what to tell the player. No training, no model.
# Runs as-is: record yourself singing or playing, or try the .wav
# files in test-files/.
#
# To make it yours:
#   1. ADAPT the numbers at the top
#   2. ADAPT the rules in check(): the messages and what counts as
#      in tune
#
# Pitch is a great job for rules: it's a measurement with an exact
# answer. Telling a violin from a flute is not, which is where a
# trained model does better.
#
# TIP: a fan or other steady hum in the room can throw the note off.
# Try somewhere quiet.
# ------------------------------------------------------------------

import gradio as gr
from measure import cents_off, loudest_part, loudness, note_of, pitch, to_samples

# ADAPT: your numbers
IN_TUNE = 10          # cents: closer than this counts as in tune (100 cents = one piano key)
TOO_QUIET = -45       # decibels: quieter than this, ask for a louder sound
TARGETS = ["A4", "E5", "D4", "G3", "C4"]   # notes the user can pick to aim for


def check(sound, target):
    if sound is None:
        return "Record or upload a sound first."
    rate, samples = to_samples(sound)
    part = loudest_part(rate, samples)
    level = loudness(part)

    # ADAPT: your rules
    if level < TOO_QUIET:
        return f"That's too quiet to hear clearly ({level:.0f} dB). Try again closer to the microphone."
    hz = pitch(rate, part)
    if hz is None:
        return "I couldn't hear a clear note. Try one long, steady note between about 60 and 1500 Hz (bass guitar to piccolo)."
    note, cents = note_of(hz)
    heard = f"I heard {note} ({hz:.1f} Hz, {cents:+d} cents)."
    if target == "Any note":
        return heard
    off = cents_off(hz, target)
    if abs(off) <= IN_TUNE:
        return f"{heard}\nIn tune with {target}. Nice!"
    if abs(off) > 50:
        return f"{heard}\nThat's a different note from {target}."
    return f"{heard}\n{'Sharp (too high)' if off > 0 else 'Flat (too low)'} by {abs(off)} cents " \
           f"(100 cents is one piano key). {'Bring it down' if off > 0 else 'Bring it up'} a little."


gr.Interface(
    fn=check,
    # ADAPT: label your inputs for your audience
    inputs=[gr.Audio(sources=["microphone", "upload"], type="numpy", label="Sing or play one steady note (or upload a .wav file)"),
            gr.Dropdown(["Any note"] + TARGETS, value="A4", label="Aim for")],
    outputs=gr.Textbox(label="Result"),
).launch(show_error=True)

# IDEAS TO TRY
# - A noise meter for the classroom: only loudness() and rules like
#   "above -20 dB for 3 seconds = too loud".
# - Play a sequence of target notes, like a simple SingStar.
