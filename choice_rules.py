# ------------------------------------------------------------------
# CHOICE RULES: a plant care advisor
# The user answers a few questions; your rules decide what to do and
# explain why. No training, no model.
#
# To make it yours:
#   1. ADAPT the questions (the inputs at the bottom)
#   2. ADAPT the rules in advise(): the numbers and the messages
#
# Tip: write your rules in plain English first, like
#   "if the soil is drier than 30%, water it",
# then turn each one into an if statement.
# ------------------------------------------------------------------

import gradio as gr

# ADAPT: the numbers your rules use. Keeping them together at the top
# makes them easy to find and change after testing.
DRY_SOIL = 30         # % moisture: below this, water it
SOGGY_SOIL = 80       # % moisture: above this, let it dry out
COLD = 10             # °C: below this, move it somewhere warmer
HOT = 32              # °C: above this, move it out of the heat


def advise(light, moisture, temperature, plant_type):
    actions, reasons = [], []

    # ADAPT: your rules. Each one adds an action AND the reason for it.
    if moisture < DRY_SOIL:
        actions.append("Water it.")
        reasons.append(f"Soil moisture {moisture}% is below {DRY_SOIL}%.")
    elif moisture > SOGGY_SOIL:
        actions.append("Don't water it for a few days.")
        reasons.append(f"Soil moisture {moisture}% is above {SOGGY_SOIL}%: roots can rot.")

    if temperature < COLD:
        actions.append("Move it somewhere warmer.")
        reasons.append(f"{temperature}°C is below {COLD}°C.")
    elif temperature > HOT:
        actions.append("Move it out of the heat.")
        reasons.append(f"{temperature}°C is above {HOT}°C.")

    if light == "Dark corner" and plant_type != "Shade lover":
        actions.append("Move it closer to a window.")
        reasons.append("Most plants need more light than a dark corner gives.")
    elif light == "Full sun all day" and plant_type == "Shade lover":
        actions.append("Give it some shade.")
        reasons.append("Shade lovers can burn in full sun.")

    # ADAPT: what to say when no rule fired
    if not actions:
        return "Your plant looks happy. Keep doing what you're doing.", "No rule needed to step in."
    return "\n".join(actions), "\n".join(reasons)


gr.Interface(
    fn=advise,
    # ADAPT: your questions. Dropdowns and sliders limit answers to ones
    # your rules can handle, which makes rules much easier to write.
    inputs=[
        gr.Dropdown(["Dark corner", "Bright room", "Full sun all day"], value="Bright room", label="Where is it?"),
        gr.Slider(0, 100, value=50, step=1, label="Soil moisture (%)"),
        gr.Slider(-5, 45, value=20, step=1, label="Temperature (°C)"),
        gr.Radio(["Shade lover", "Sun lover", "Not sure"], value="Not sure", label="What kind of plant?"),
    ],
    outputs=[gr.Textbox(label="What to do"), gr.Textbox(label="Why")],
).launch(show_error=True)

# IDEAS TO TRY
# - Same pattern, different problem: waste sorting by what an item is
#   made of, a "which study method?" helper, a weather clothing advisor.
# - Test the edges: what happens at exactly 30%? Is that what you want?
