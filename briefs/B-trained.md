# Brief B: Trained pattern detector

Build a Python app that recognises **your own** groups of pictures, body poses or sounds, using a model you train
yourself.

## Why train a model?

Some things are easy for people to recognise but almost impossible to describe as rules. Think about a cat and a dog:
every breed, angle and lighting would need its own rule. Instead, you show the computer lots of examples of each
group, and it finds its own patterns. Then it uses those patterns on things it has never seen.

## What you'll do

1. **Pick a problem and a user.** Write one sentence: who is it for, and what will it tell them?
2. **Plan your classes.** Two to five groups, plus a "nothing" class if your app will often see none of them.
3. **Train it** in the [Pattern Trainer](https://tools.learningwaypoints.com/trainer/). Its
   [guide](https://tools.learningwaypoints.com/trainer/guide.html) walks you through collecting examples, training
   and checking.
4. **Try to fool it.** Test it in new places, with new people (who said yes), and with things that aren't any of
   your classes. Record what happens.
5. **Build the app.** Put your model file in this folder and adapt the starter for your mode:
   `image_pattern_trainer.py`, `pose_pattern_trainer.py` or `audio_pattern_trainer.py`.
6. **Choose a confidence threshold.** Below it, your app should say it isn't sure rather than guess. Use your testing
   to pick the number.
7. **Try the other way.** Name one thing in your project a simple rule would do better than the model, and say why.

## Ideas

**Pictures**
- A recycling helper: which bin does this go in?
- A plant check: does this leaf look healthy or not?
- A hand-sign counter for a younger sibling learning numbers.
- A Lego sorter: which kind of brick is this?

**Body poses**
- A squat or plank form coach.
- A posture reminder that notices slouching.
- A gesture remote: arms up for the next slide.
- A dance move checker.

**Sounds**
- Clap or click commands for an app.
- An appliance listener: the microwave, the doorbell or the kettle?
- An instrument identifier.
- A vocabulary trainer that hears words in another language.

## What to hand in

- **Your app:** the `.py` file and your model file.
- **Testing record:** a table with the input, what you expected, what the app said and how sure it was. Include at
  least five inputs it hadn't seen before, and at least two things that aren't any of your classes.
- **Reflection:** what fooled it, and what you changed because of it (more examples, a new class, a different
  threshold), the rule-versus-model point from step 7, and who could be affected if your app got it wrong.

## Check your app

- **Clear result** in words your user understands.
- **Honest confidence:** says when it isn't sure.
- **Useful response:** advice, a next step or a score, not just a label.
- **Fits your user:** at least one setting or option they can change.
- **Tested** on things you didn't train it on.

## Good habits

Only record yourself, or people who have said yes. Check what's behind you before you record. Your pictures and
sounds stay on your computer; only the trained numbers go in the model file.
