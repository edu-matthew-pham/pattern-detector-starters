# Test files

Photos for checking the starters run before you adapt them.

With the sample `my_model.json` (run `image_pattern_trainer.py`):

| File | Expect |
|---|---|
| `cat.jpg` | Cat |
| `coffee.jpg` | Coffee |

Then try something that is neither, like your hand or a book. The model still has to pick Cat or Coffee,
and it may be very sure about it. That's worth thinking about when you design your own classes.

With the sample `my_pose_model.json` (run `pose_pattern_trainer.py`):

| File | Expect |
|---|---|
| `person_upright.jpg` | Upright |
| `person_leaning.jpg` | Leaning |
| `cat.jpg` | "I can't see a person" |

**Credits:** all four photos come from the [scikit-image](https://scikit-image.org) sample data and are free to
reuse. `cat.jpg` (Stefan van der Walt) and `coffee.jpg` (Rachel Michetti) are CC0. `person_upright.jpg` and
`person_leaning.jpg` (rotated) are the astronaut photo of Eileen Collins (NASA, public domain).
