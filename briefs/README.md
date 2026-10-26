# Pattern Detector briefs

A **pattern detector** is an app that sorts an input (some text, a photo, a pose, a sound) into groups and responds
in a useful way. There are two ways to build the sorting part, and a third project that uses both.

| Brief | How it sorts | When |
|---|---|---|
| [A. Rules](A-rules.md) | You write the rules yourself, with `if` statements and lookups | Any order |
| [B. Trained](B-trained.md) | You train a model on examples in the [Pattern Trainer](https://tools.learningwaypoints.com/trainer/) | Any order |
| [C. Combined](C-combined.md) | A trained model feeds your rules | After A and B |

A and B stand on their own, so your teacher may start with either one, or let you choose. Each ends with a short
step that looks at the other way, so you'll be ready for C.

## The big idea

Some problems suit rules. You can say exactly what to check: if the message contains "no cap", it means "honestly".
Rules are easy to explain and easy to fix.

Other problems have far too many details for rules. You can tell a cat from a dog in a split second, but try writing
the rules: every breed, angle, colour and lighting. You'd never finish. Machine learning handles this by learning
from lots of examples, then using what it learned on things it has never seen. The trade-off: it can be very sure and
still wrong, and it can't tell you why.

## Every brief: make it useful for a real person

Whichever brief you do, your app is for someone. Before you build, write one sentence: *who is it for, and what
problem does it solve for them?* Then check your app against this list:

- **Clear result:** says what it found in words your user understands, not just a label.
- **Honest confidence:** shows how sure it is, or says when it can't tell, instead of guessing.
- **Useful response:** does something with the result (advice, a next step, a score), not just reports it.
- **Fits your user:** settings, toggles or inputs that let them make it their own.
- **Tested:** you've tried it with inputs you didn't design it around, and kept a record.
