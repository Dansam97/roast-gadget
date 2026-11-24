#!/usr/bin/env python3
"""Entry for the make.fun bounty "One-Line Roast: The Gadget You Use Every Day"
(u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610).

Writes one roast line about a gadget used every day to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

TEXT = (
    "My smartwatch congratulates me for standing up, then two minutes later "
    "reminds me to breathe, as if standing was the achievement and "
    "breathing is the sequel it doesn't trust me to survive alone."
)


MAX_CHARS = 200


def validated_text() -> str:
    """Return TEXT after checking it against the bounty gate.

    The gate accepts UTF-8 text of 1 to 200 characters that is not only
    white space; the entry must also be exactly one line.
    """
    text = TEXT
    encoded = text.encode("utf-8")  # raises if not encodable
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry text is {len(text)} chars, outside 1..{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry text is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if len(encoded) != len(text.encode("utf-8")):
        raise ValueError("encoding check failed")
    return text


def main() -> None:
    text = validated_text()
    payload = (text + "\n").encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(payload)
    with open(path, "rb") as fh:
        written = fh.read()
    if written != payload:
        raise IOError("entry.txt read-back does not match the payload")


if __name__ == "__main__":
    main()
