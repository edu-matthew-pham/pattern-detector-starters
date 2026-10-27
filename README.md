# Pattern Detector Starters

Working starter apps for building your own pattern detector: a small app that sorts an input into your own
classes. Each starter runs as-is, then you change the lines marked `# ADAPT:` to make it yours.

| Your idea involves... | Start from |
|---|---|
| Recognising YOUR own categories in photos, trained in the [Pattern Trainer](https://tools.learningwaypoints.com/trainer/) | `image_pattern_trainer.py` |
| Recognising YOUR own body poses (exercise form, gestures, dance moves), trained in the [Pattern Trainer's Body poses mode](https://tools.learningwaypoints.com/trainer/?mode=pose) | `pose_pattern_trainer.py` |
| Recognising YOUR own sounds (spoken words, claps, instruments, machine noises), trained in the [Pattern Trainer's Sounds mode](https://tools.learningwaypoints.com/trainer/?mode=audio) | `audio_pattern_trainer.py` |

## Set up (once)

You need Python 3 on your computer (tested with Python 3.13). In a terminal, in this folder:

**Windows**
```
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**macOS / Linux**
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The install is about 0.5 GB and doesn't need TensorFlow.

## Run it

```
python image_pattern_trainer.py
```

Open the address it prints (usually `http://127.0.0.1:7860`) and try the photos in `test-files/`.
For poses, run `python pose_pattern_trainer.py`; for sounds, `python audio_pattern_trainer.py`.

## Make it yours

1. Open the [Pattern Trainer](https://tools.learningwaypoints.com/trainer/), make your classes,
   add examples, train and test.
2. Click **Download my_model.json** (or **my_pose_model.json** / **my_audio_model.json** in Body poses / Sounds
   mode) and move it into this folder, replacing the sample.
3. Run the starter again. Your class names come from the file, so there's nothing to type.
4. Change the `# ADAPT:` lines: your messages, your confidence threshold, your labels.
5. Rename the file to match your project.

## What's in this folder

| File | What it is | Edit it? |
|---|---|---|
| `image_pattern_trainer.py` | The app | Yes, the `# ADAPT:` lines |
| `pose_pattern_trainer.py` | The body-pose app | Yes, the `# ADAPT:` lines |
| `my_model.json` | The trained model: class names and the trained numbers. Sample: Cat vs Coffee | Replace with yours |
| `my_pose_model.json` | A trained pose model. Sample: Upright vs Leaning | Replace with yours |
| `audio_pattern_trainer.py` | The sound app | Yes, the `# ADAPT:` lines |
| `my_audio_model.json` | A trained sound model. Sample: Background noise / Beep / Knock | Replace with yours |
| `pattern_model.py` | Loads your model file and prepares photos, poses and sounds exactly as the Pattern Trainer does | No (but have a look inside) |
| `mobilenet_v2_embedder.tflite` | The shared image model that turns a photo into 1280 numbers | No |
| `pose_landmarker_lite.task` | The shared pose model that finds 33 body points in a photo | No |
| `yamnet.tflite` | The shared sound model (YAMNet) that scores each second of sound against 521 kinds of sound | No |
| `test-files/` | Photos and sounds to check the starters run | Add your own |

**Curious how it works?** `model.embed(image)` shows the numbers the trained part sees for a photo (1280 for
pictures, 66 for poses, 521 per second for sounds), `pattern_model.pose_points(image)` gives the 33 body points,
`pattern_model.sound_windows(sound)` shows what YAMNet heard each second, and
`model.predict(image)` shows the confidence for every class. `pattern_model.py` runs the trained part with a
few lines of numpy you can read.

## Project briefs

What to build, and what to hand in: see [`briefs/`](briefs/README.md). There are three: rules you write yourself (A),
a model you train (B), in either order, then both together (C).

### Rules starters (Brief A)

No model file needed: these run straight away, and you write the rules.

| Starter | What it does | Try it with |
|---|---|---|
| `text_rules.py` | Decodes phrases in a message using a dictionary you write | `ngl idk what brb means lol` |
| `choice_rules.py` | Plant care advice from a few questions, with the reason for each rule | The sliders |
| `colour_rules.py` | Fruit ripeness from how much of the photo is green, yellow or brown | `test-files/fruit_*.jpg`, then `cat.jpg` |
| `sound_rules.py` | Which note you sang or played, and whether it's sharp or flat | `test-files/note_a4*.wav` |
| `measure.py` | The measuring tools for colours and sounds (loudness, pitch, colour shares) | No need to edit |

## If something goes wrong

- **"Can't find 'my_model.json'"**: the file has to be in the same folder as the starter, named exactly
  `my_model.json`. Browsers sometimes save a second download as `my_model (1).json`.
- **"Can't find the image model"**: keep `mobilenet_v2_embedder.tflite` in this folder.
- **"Ask your teacher for the latest starter"**: your `my_model.json` came from a newer Pattern Trainer than this
  copy of the starters. Download the latest starters.
- **"I can't see a person"** (poses): stand back so your whole body is in view, with good light.
- **Sound files won't load** (sounds): use `.wav` files, or record in the app. Other formats need extra software.
- **Webcam doesn't show**: allow camera access in the browser, and close other apps using the camera.

## Acknowledgements

Models come from the [Pattern Trainer](https://tools.learningwaypoints.com/trainer/), which is inspired by Google's
[Teachable Machine](https://teachablemachine.withgoogle.com/). The starters use Google's
[MediaPipe](https://ai.google.dev/edge/mediapipe) and [Gradio](https://www.gradio.app/). Made by Matthew Pham with help from
Claude (Anthropic).

## Licences

Free for teachers, students, schools and other non-commercial use under the [PolyForm Noncommercial License 1.0.0](LICENSE); commercial use needs permission (contact [Matthew Pham on GitHub](https://github.com/edu-matthew-pham)). Copyright 2026 Matthew Pham. The image model is MobileNetV2 (Keras Applications, Apache-2.0); the pose model is Google's MediaPipe Pose
Landmarker and the sound model is Google's YAMNet (both Apache-2.0). Test photos are CC0; see `test-files/README.md`.
