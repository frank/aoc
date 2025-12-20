import os
from pathlib import Path
from shutil import copyfile


def touch(path: Path):
    with open(path, "a"):
        os.utime(path, None)


if __name__ == "__main__":
    year = 2025
    day = 12

    root_dir = Path(__file__).parent / str(year)
    txt_dir = root_dir / "inputs"

    # make input files
    touch(txt_dir / f"day_{day}.txt")
    touch(txt_dir / f"day_{day}_test.txt")

    # copy template to new day
    copyfile(root_dir.parent / "template.py", root_dir / f"day_{day}.py")
