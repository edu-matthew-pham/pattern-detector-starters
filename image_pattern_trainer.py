# ------------------------------------------------------------------
# IMAGE CLASSIFIER (your own Pattern Trainer model)
# Runs with the included my_model.json (Cat vs Coffee) so you can see
# it work, then you replace that with YOUR download.
#
# To make it yours:
#   1. Train your classes in the Pattern Trainer:
#      https://tools.learningwaypoints.com/trainer/
#   2. Click "Download my_model.json"
#   3. Move YOUR my_model.json into this folder (replace the sample)
#   4. ADAPT the responses and threshold
#
# You don't need to type your class names: they're saved inside
# my_model.json, in the right order, so they can't get mixed up.
#
# TIP: if you trained with the webcam, test with the webcam too.
# A model trained in one spot often does worse on photos taken
# somewhere else, because it partly learned the background.
# ------------------------------------------------------------------

import gradio as gr
import os
from pattern_model import PatternModel

# Look for the model file next to this script, so it works no matter
# which folder you run from
MODEL_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "my_model.json")

# pattern_model.py does the fixed steps for you, exactly as the
# Pattern Trainer did them: cut the photo to its centre square, turn
# it into numbers with the same image model, then run your trained part.
model = PatternModel.load(MODEL_FILE)
print("Classes in this model:", model.classes)

def classify(image):
    if image is None:
        return "Upload or take a photo first."
    # top() gives the most likely class and how sure the model is (0 to 1)
    label, score = model.top(image)
    # ADAPT: your threshold and messages
    # Heads up: models are often very sure even when they're wrong, so
    # test with photos it hasn't seen before trusting the threshold.
    if score < 0.8:
        return f"Might be {label}, but I'm not confident ({score:.2f})."
    else:
        return f"{label} ({score:.2f} confidence)"

gr.Interface(
    fn=classify,
    # ADAPT: label your input for your audience
    # mirror=False keeps left and right the same way round as in the
    # Pattern Trainer, so a model trained with your webcam matches here.
    # image_mode="RGBA" lets see-through PNGs reach pattern_model.py,
    # which treats see-through areas as white, like the trainer does.
    inputs=gr.Image(type="pil", sources=["upload", "webcam"], label="Upload or take a photo:",
                    image_mode="RGBA", webcam_options=gr.WebcamOptions(mirror=False)),
    outputs="text"
).launch(show_error=True)

# WANT BARS FOR EVERY CLASS, like the Pattern Trainer's test panel?
# Make a function that returns model.predict(image) (a dictionary of
# class: confidence) and use outputs=gr.Label() instead of "text".

# WANT LIVE VIDEO INSTEAD?
# Swap the whole gr.Interface block above for this one. It classifies
# continuously as the camera runs, instead of one photo at a time.
# Heads up: it runs the model on every frame, so it can be slow,
# so test it before relying on it for a demo.
#
# gr.Interface(
#     fn=classify,
#     inputs=gr.Image(type="pil", sources=["webcam"], streaming=True, label="Point the camera:",
#                     image_mode="RGBA", webcam_options=gr.WebcamOptions(mirror=False)),
#     outputs="text",
#     live=True
# ).launch(show_error=True)
