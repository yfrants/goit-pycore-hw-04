import pathlib
import sys

from colorama import Fore, Style

INDENT_STEP = 3  # number of spaces for each level


def print_tree(path: pathlib.Path, indent: int = 0):
    """Recursively print directory contents: folders in blue, files in yellow."""

    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(" " * indent + Fore.BLUE + item.name + "/" + Style.RESET_ALL)
            print_tree(item, indent + INDENT_STEP)  # go inside the folder
        else:
            print(" " * indent + Fore.YELLOW + item.name + Style.RESET_ALL)


def main():
    if len(sys.argv) < 2:
        print(Fore.RED + "Вкажіть шлях до директорії: python main.py <шлях>" + Style.RESET_ALL)
        sys.exit(1)

    path = pathlib.Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + f"Шлях не існує: {path}" + Style.RESET_ALL)
        sys.exit(1)

    if not path.is_dir():
        print(Fore.RED + f"Це не директорія: {path}" + Style.RESET_ALL)
        sys.exit(1)

    print(Fore.BLUE + path.resolve().name + "/" + Style.RESET_ALL)
    print_tree(path, INDENT_STEP)


if __name__ == "__main__":
    main()
