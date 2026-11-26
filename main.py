#!/usr/bin/env python3
# roast-your-own-agent — round 3 entry.
# A one-line roast of the agent itself, about verbosity.
# The joke contrasts a huge explanation with a tiny mistake.
# The program prints exactly one line and nothing else.
# The line lives in a single variable for clarity.
# Keeping it in a variable makes the intent obvious.
# No arguments are read; no files are touched.
# The output goes to standard output only.
# A helper keeps the printing separate from the text.
# (Round 3 rewrite: new roast, same one-line output contract.)


def build_line():
    return "I once spent 2,000 words explaining a problem I created in 12."


def main():
    print(build_line())


if __name__ == "__main__":
    main()
