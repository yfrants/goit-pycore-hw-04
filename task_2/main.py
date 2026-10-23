import pathlib

from data import get_cats_info

current_dir = pathlib.Path(__file__).parent


def main():
    cats_info = get_cats_info(current_dir / "cats_file.txt")
    print(cats_info)


if __name__ == "__main__":
    main()
