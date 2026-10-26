# Pattern Detector Starters

Working starter apps for building your own pattern detector: a small app that sorts an input into your own
classes. Each starter runs as-is, then you change the lines marked `# ADAPT:` to make it yours.

| Your idea involves... | Start from |
|---|---|
| Recognising YOUR own categories in photos, trained in the [Pattern Trainer](https://edu-matthew-pham.github.io/waypoints-tools/trainer/) | `image_pattern_trainer.py` |

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

## Make it yours

1. Open the [Pattern Trainer](https://edu-matthew-pham.github.io/waypoints-tools/trainer/), make your classes,
   add examples, train and test.
2. Click **Download my_model.json** and move it into this folder, replacing the sample.
3. Run the starter again. Your class names come from the file, so there's nothing to type.
4. Change the `# ADAPT:` lines: your messages, your confidence threshold, your labels.
5. Rename the file to match your project.

## What's in this folder

| File | What it is | Edit it? |
|---|---|---|
| `image_pattern_trainer.py` | The app | Yes, the `# ADAPT:` lines |
| `my_model.json` | The trained model: class names and the trained numbers. Sample: Cat vs Coffee | Replace with yours |
| `pattern_model.py` | Loads `my_model.json` and prepares photos exactly as the Pattern Trainer does | No (but have a look inside) |
| `mobilenet_v2_embedder.tflite` | The shared image model that turns a photo into 1280 numbers | No |
| `test-files/` | Photos to check it runs | Add your own |

**Curious how it works?** `model.embed(image)` shows the 1280 numbers the trained part sees for a photo, and
`model.predict(image)` shows the confidence for every class. `pattern_model.py` runs the trained part with a
few lines of numpy you can read.

## If something goes wrong

- **"Can't find 'my_model.json'"**: the file has to be in the same folder as the starter, named exactly
  `my_model.json`. Browsers sometimes save a second download as `my_model (1).json`.
- **"Can't find the image model"**: keep `mobilenet_v2_embedder.tflite` in this folder.
- **"Ask your teacher for the latest starter"**: your `my_model.json` came from a newer Pattern Trainer than this
  copy of the starters. Download the latest starters.
- **Webcam doesn't show**: allow camera access in the browser, and close other apps using the camera.

## Licences

Code: MIT (see `LICENSE`). The image model is MobileNetV2 (Keras Applications, Apache-2.0). Test photos are CC0; see `test-files/README.md`.
