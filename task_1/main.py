import pathlib

from processing import total_salary

current_dir = pathlib.Path(__file__).parent


def main():
    total, average = total_salary(current_dir / "salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


if __name__ == "__main__":
    main()
