def load_data(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def clean_data(lines: list[str]) -> list[int]:
    salaries = []
    for line in lines:
        line = line.strip()
        if not line:
            continue

        try:
            _, salary = line.split(",")
            salaries.append(int(salary))
        except ValueError:
            print(f"Некоректний рядок пропущено: {line}")

    return salaries
