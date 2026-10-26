# ------------------------------------------------------------------
# SOUND CLASSIFIER (your own Pattern Trainer sound model)
# Runs with the included my_audio_model.json (Background noise / Beep /
# Knock) so you can see it work, then you replace that with YOUR download.
#
# To make it yours:
#   1. Train your sounds in the Pattern Trainer (Sounds mode):
#      https://tools.learningwaypoints.com/trainer/?mode=audio
#   2. Click "Download my_audio_model.json"
#   3. Move YOUR my_audio_model.json into this folder (replace the sample)
#   4. ADAPT the responses and threshold
#
# Only YAMNet's 521 sound scores are used, about one set per second.
# A longer recording is scored each second and the results averaged.
#
# TIP: record your examples in the same room (and with the same
# microphone) you'll use the app in. Background noise matters.
# ------------------------------------------------------------------

import gradio as gr
import os
from pattern_model import PatternModel

# Look for the model file next to this script, so it works no matter
# which folder you run from
MODEL_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "my_audio_model.json")

# pattern_model.py does the fixed steps for you, exactly as the
# Pattern Trainer did them: turn each second of sound into YAMNet's
# 521 sound scores, then run your trained part.
model = PatternModel.load(MODEL_FILE)
print("Sounds in this model:", model.classes)

def classify(sound):
    # Gradio gives (sample_rate, samples); pattern_model.py handles both
    if sound is None:
        return "Record or upload a sound first."
    label, score = model.top(sound)
    if label is None:
        return "That recording was empty. Try again."
    # ADAPT: your threshold and messages
    # Heads up: models are often very sure even when they're wrong, so
    # test with sounds it hasn't heard before trusting the threshold.
    if score < 0.8:
        return f"Might be {label}, but I'm not confident ({score:.2f})."
    else:
        return f"{label} ({score:.2f} confidence)"

gr.Interface(
    fn=classify,
    # ADAPT: label your input for your audience
    inputs=gr.Audio(sources=["microphone", "upload"], type="numpy", label="Record or upload a sound:"),
    outputs="text"
).launch(show_error=True)

# WANT BARS FOR EVERY CLASS, like the Pattern Trainer's test panel?
# Make a function that returns model.predict(sound) (a dictionary of
# class: confidence) and use outputs=gr.Label() instead of "text".
