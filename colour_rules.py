# ------------------------------------------------------------------
# COLOUR RULES: a fruit ripeness checker
# Measures how much of a photo is each colour, then YOUR rules decide
# what that means. No training, no model.
# Runs as-is: try the fruit photos in test-files/.
#
# To make it yours:
#   1. ADAPT the COLOURS you measure (hue ranges on the colour wheel)
#   2. ADAPT the rules in check(): the shares and the messages
#
# Every colour has a position on a colour wheel, measured in degrees.
# That position is called its hue. The second picture shows exactly
# which pixels were counted, in their own colour. Use it to tune your
# hue ranges.
#
# Rules like these work well when you control the conditions: a plain
# background and steady light. Try it somewhere messy and see what
# happens. That's where a trained model can do better.
# ------------------------------------------------------------------

import gradio as gr
from measure import colour_shares

# ADAPT: the colours you measure, as hue ranges in degrees.
# The colour wheel: red 0, orange 30, yellow 60, green 120, cyan 180,
# blue 240, purple 280, red again at 360. "dark" means very dark pixels.
# Very dark pixels (shadows, a black background) aren't counted unless
# you add  "dark": "dark"  to this list.
COLOURS = {
    "green": (75, 160),
    "yellow": (40, 75),
    "brown": (10, 40),
}


def check(image):
    if image is None:
        return "Upload or take a photo first.", None
    shares, preview = colour_shares(image, COLOURS)
    green, yellow = shares["green"], shares["yellow"]
    spots = shares["brown"]
    report = ", ".join(f"{name} {share:.0%}" for name, share in shares.items())

    # ADAPT: your rules. Check the most specific case first.
    if green + yellow + spots < 0.3:
        verdict = "I can't see much fruit colour. Try a plain background."
    elif spots > 0.25:
        verdict = "Very ripe: good for baking or smoothies."
    elif green > yellow:
        verdict = "Not ripe yet: give it a few days."
    elif spots > 0.05:
        verdict = "Ripe, with a few spots: eat it soon."
    else:
        verdict = "Ripe and ready."
    return f"{verdict}\n\nMeasured: {report}", preview


gr.Interface(
    fn=check,
    # ADAPT: label your input and outputs for your audience
    inputs=gr.Image(type="pil", sources=["upload", "webcam"], label="Photo of the fruit"),
    outputs=[gr.Textbox(label="Result"), gr.Image(label="What was measured")],
).launch(show_error=True)

# IDEAS TO TRY
# - Same pattern: is the traffic light red or green? Which coloured
#   card is the user holding up? Is the water clear or murky?
# - measure.brightness(image) gives 0 (black) to 100 (white): a rule
#   could say "too dark, turn on a light" before checking colours.
