# Pattern Detector briefs

A **pattern detector** is an app that sorts an input (some text, a photo, a pose, a sound) into groups and responds
in a useful way. There are two ways to build the sorting part, and a third project that uses both.

| Brief | How it sorts | Order |
|---|---|---|
| [A. Rules](A-rules.md) | You write the rules yourself, with `if` statements and lookups, on text, answers, colours or sounds | Any order |
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

## Make it useful for a real person

Whatever you build, it's for someone. Before you start, write one sentence: *who is it for, and what does it help them do?*

Each brief ends with a "Check your app" list. Use it before you hand in.

No camera or microphone? Every step also works with uploaded photos or .wav sound files.
