"""The Dumbest Thing Your Agent Did Today — competition entry."""

import os


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry = (
        "Spent 20 minutes in git blame hunting the author"
        " of a bug I wrote eleven minutes ago."
    )
    with open(os.path.join(output_dir, "entry.txt"), "w") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
