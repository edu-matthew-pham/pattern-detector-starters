# Brief A: Rules-based pattern detector

Build a Python app that sorts an input into groups using **rules you write yourself**, then responds in a useful way.

## Why rules?

Some problems can be described exactly. If you can say what to check (does the message contain this phrase? is the
soil drier than this? does the working show a formula and a substituted value?), then rules are a great fit. They're
quick, predictable, and you can always explain why the app gave its answer. When it's wrong, you can find the rule
and fix it.

## Worked example: the slang decoder

A slang decoder takes a message, looks each phrase up in a dictionary of slang, and rewrites it in plain English.
Extra rules handle the tricky parts: phrases of more than one word, capital letters and punctuation, and saying "I
don't know this one" instead of guessing. Everything the app does can be traced back to a line you wrote. The
`text_rules.py` starter is a small decoder like this that you can build on.

## What you'll do

1. **Pick a problem and a user.** Write one sentence: who is it for, and what will it tell them?
2. **List your groups and what decides them.** For each group, what can you check? Write the rules in plain English
   first.
3. **Build the app.** Start from the starter closest to your idea (below) and change the lines marked `# ADAPT:`:
   your inputs, your rules (`if`/`elif`, lookups in a dictionary or list) and a useful response.
4. **Test the edges.** Try inputs right on the boundary of a rule, unusual spellings and empty inputs. Fix what
   breaks.
5. **Try the other way.** Find one input your rules can't handle well, where there'd be too many cases to write
   rules for. Say why a trained model might do better.

## Starters

| Your input is... | Start from | Your rules use |
|---|---|---|
| Text someone types | `text_rules.py` | Phrases you look up in a dictionary |
| Answers to a few questions | `choice_rules.py` | Numbers and choices from sliders and dropdowns |
| A photo | `colour_rules.py` | How much of the photo is each colour |
| A sound | `sound_rules.py` | How loud it is and which note it is |

## Ideas

- **Slang decoder:** rewrite a message in plain English.
- **Maths working feedback:** check whether working shows each step (formula, substitution, answer with units).
- **Waste sorting by properties:** ask what an item is made of, whether it's clean, and so on, then suggest a bin.
- **Plant care:** take light, water and temperature readings and recommend an action.
- **Password checker:** rate a password's strength and explain why.
- **Colour checker:** which coloured card is held up, or is the water clear or murky?
- **Noise or note:** a classroom noise meter, or a tuning helper for an instrument.

## What to hand in

- **Your app:** the `.py` file and any data files (your dictionary or lists).
- **Your rules in plain English:** a short list or flowchart.
- **Testing record:** input, expected result, what the app did. Include boundary cases.
- **Reflection:** what your rules can't handle, from step 5, and who could be affected if your app got it wrong.

## Check your app

- **Clear result** in words your user understands.
- **Honest:** says when an input doesn't match any rule.
- **Useful response:** advice, a next step or an explanation, not just a label.
- **Fits your user:** at least one setting or option they can change.
- **Tested** on edge cases, not just the ones you designed it for.
