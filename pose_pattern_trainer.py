# ------------------------------------------------------------------
# BODY POSE CLASSIFIER (your own Pattern Trainer pose model)
# Runs with the included my_pose_model.json (Upright vs Leaning) so you
# can see it work, then you replace that with YOUR download.
#
# To make it yours:
#   1. Train your poses in the Pattern Trainer (Body poses mode):
#      https://tools.learningwaypoints.com/trainer/?mode=pose
#   2. Click "Download my_pose_model.json"
#   3. Move YOUR my_pose_model.json into this folder (replace the sample)
#   4. ADAPT the responses and threshold
#
# Only 33 body points are used, not the picture itself. The model needs
# to see a person: if nobody is found, top() gives (None, 0.0).
#
# TIP: stand back so your whole body is in view, like when you trained.
# ------------------------------------------------------------------

import gradio as gr
import os
from pattern_model import PatternModel

# Look for the model file next to this script, so it works no matter
# which folder you run from
MODEL_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "my_pose_model.json")

# pattern_model.py does the fixed steps for you, exactly as the
# Pattern Trainer did them: find the 33 body points, turn them into
# numbers, then run your trained part.
model = PatternModel.load(MODEL_FILE)
print("Poses in this model:", model.classes)

def classify(image):
    if image is None:
        return "Upload or take a photo first."
    label, score = model.top(image)
    if label is None:
        # ADAPT: what to say when nobody is in the picture
        return "I can't see a person. Step back so your whole body is in view."
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
    # Pattern Trainer, so "left arm up" stays the left arm.
    inputs=gr.Image(type="pil", sources=["webcam", "upload"], label="Strike a pose:",
                    image_mode="RGBA", webcam_options=gr.WebcamOptions(mirror=False)),
    outputs="text"
).launch(show_error=True)

# WANT LIVE VIDEO INSTEAD, for exercise counting or a pose game?
# Swap the whole gr.Interface block above for this one. It classifies
# continuously as the camera runs. Heads up: it runs the model on every
# frame, so test the speed on your computer first.
#
# gr.Interface(
#     fn=classify,
#     inputs=gr.Image(type="pil", sources=["webcam"], streaming=True, label="Move!",
#                     image_mode="RGBA", webcam_options=gr.WebcamOptions(mirror=False)),
#     outputs="text",
#     live=True
# ).launch(show_error=True)
