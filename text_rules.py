# ------------------------------------------------------------------
# TEXT RULES: a phrase decoder
# Sorts and rewrites text using rules YOU write: no training, no model.
# Runs as-is with a small set of texting abbreviations, then you swap
# in your own phrases and rules.
#
# To make it yours:
#   1. ADAPT the PHRASES dictionary: what to look for, what it means
#   2. ADAPT the rules in decode() and the messages
#
# Everything this app says can be traced back to a line you wrote.
# That's the big strength of rules: you can always explain the answer.
# ------------------------------------------------------------------

import gradio as gr
import re

# ADAPT: your phrases. Keys are what to look for (lower case);
# values are what they mean. Phrases can be more than one word.
PHRASES = {
    "brb": "be right back",
    "idk": "I don't know",
    "tbh": "to be honest",
    "imo": "in my opinion",
    "ngl": "not going to lie",
    "lol": "(laughing)",
    "np": "no problem",
    "ty": "thank you",
    "on my way": "coming now",
    "low key": "a little bit / secretly",
}

# Longest phrases first, so "on my way" is found before shorter phrases inside it.
ORDER = sorted(PHRASES, key=len, reverse=True)


def find_phrases(text):
    """Every known phrase in the text, as (start, end, phrase), left to right, no overlaps."""
    found, taken = [], set()
    lower = text.lower()
    for phrase in ORDER:
        # \b means "word edge", so "ty" isn't found inside "party"
        for m in re.finditer(r"\b" + re.escape(phrase) + r"\b", lower):
            span = set(range(m.start(), m.end()))
            if not span & taken:
                found.append((m.start(), m.end(), phrase))
                taken |= span
    return sorted(found)


def decode(text):
    text = (text or "").strip()
    # ADAPT: what to say when there's nothing to work with
    if not text:
        return "Type a message first.", ""
    found = find_phrases(text)
    if not found:
        return text, "I didn't find any phrases I know in that message."

    # Rebuild the message with each phrase replaced by its meaning
    plain, last = "", 0
    for start, end, phrase in found:
        meaning = PHRASES[phrase]
        if text[start].isupper():       # keep a capital letter, e.g. at the start of a sentence
            meaning = meaning[0].upper() + meaning[1:]
        plain += text[last:start] + meaning
        last = end
    plain += text[last:]

    # ADAPT: your rules about the message as a whole
    share = sum(end - start for start, end, _ in found) / len(text)
    if share > 0.5:
        note = "That message is mostly abbreviations!"
    elif len(found) == 1:
        note = "Found 1 phrase."
    else:
        note = f"Found {len(found)} phrases."
    explained = "\n".join(f"• {text[s:e]} → {PHRASES[p]}" for s, e, p in found)
    return plain, f"{note}\n{explained}"


gr.Interface(
    fn=decode,
    # ADAPT: label your input and outputs for your audience
    inputs=gr.Textbox(label="Message to decode", placeholder="ngl idk what brb means lol"),
    outputs=[gr.Textbox(label="In plain English"), gr.Textbox(label="What I found")],
).launch(show_error=True)

# IDEAS TO TRY
# - Sort messages instead of rewriting them: e.g. count "kind" and
#   "unkind" phrases and return which one wins (and say when it's a tie).
# - Load PHRASES from a .csv file so it's easy to add more.
# - Add a dropdown for "who's reading" and change the wording to suit.
