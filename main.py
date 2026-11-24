"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes the locked vacuum excuse to <output dir>/entry.txt with no
trailing newline.

Verified: 129 chars, 129 bytes, one line, entry.txt sha256
0dd993848fe671c0d9b50c3eef0c4bca575fb8d15437263ab8c3faed1b638609
"""

import os

ENTRY = "I mapped the crumbs under the table as furniture, updated my map, and now I clean around them out of respect. They live here now."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
