# Brief C: Combined pattern detector

**Before you start:** you've built one rules-based app ([Brief A](A-rules.md)) and one trained app
([Brief B](B-trained.md)).

Build an app where **a trained model recognises something, and your rules decide what to do about it.** Each part
does the job it's best at: the model handles the messy, real-world input, and the rules handle the parts you can
describe exactly.

## How the two parts fit

```
input  →  trained model  →  label + how sure  →  your rules  →  response
(photo, pose, sound)         ("Plank", 0.92)      (if, lookups,     (advice, a score,
                                                   settings)         a next step)
```

Your rules should use the confidence too. What does your app do when the model isn't sure?

## Ideas

- **Recipe helper:** a model recognises ingredients in a photo; rules suggest a recipe that fits the user's dietary
  needs.
- **Singing or playing coach:** a model recognises the instrument; rules work out the note being played from its
  pitch and check it against the song (like SingStar).
- **Language revision:** a model hears a word spoken in another language; a rules-based dictionary shows or says the
  English meaning and keeps score.
- **Workout timer:** a model recognises the exercise pose; rules count time in the pose and only count it when the
  form is right.
- **Local recycling guide:** a model recognises the item; rules apply the recycling rules for the user's council.

## What you'll do

1. **Pick a problem and a user.** Write one sentence: who is it for, and what will it do for them?
2. **Draw your pipeline** like the diagram above. Label which part is trained and which is rules, and say why each
   part is done that way.
3. **Build and test each part on its own,** then join them.
4. **Test the joins.** What happens when the model is wrong, or unsure? Make sure the rules handle it sensibly.

## What to hand in

- **Your app:** the `.py` file, model file and any data files.
- **Pipeline diagram** with the reason for each part.
- **Testing record** for each part and for the whole app, including inputs where the model was unsure or wrong.
- **Reflection:** which part caused the most problems, what you'd change, and who could be affected if your app got
  it wrong.

## Check your app

- **Clear result** in words your user understands.
- **Honest confidence:** low-confidence results are handled, not hidden.
- **Useful response** that needs both parts.
- **Fits your user:** settings or options they can change.
- **Tested** as a whole, not just part by part.
