"""The Dog Ate My Homework — make.fun entry.

Writes one line — a dog explaining why it ate the homework, in the
dog's own voice after being caught — to /output/entry.txt.
"""

import os

EXCUSE = (
    "I ate it because you kept telling people 'the dog ate my homework' "
    "like it was a joke, so I finally made one of your stories true."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
