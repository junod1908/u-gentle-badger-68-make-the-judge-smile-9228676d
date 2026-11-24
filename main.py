"""Make the Judge Smile — one line about a small good thing that happened today.

Writes the entry to /output/entry.txt (1-200 characters, UTF-8).
"""

ENTRY = "The barber who's cut my hair for ten years finally told me today why he always hums the same song: 'Your father used to whistle it in this chair.'"

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
