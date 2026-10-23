def load_data(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def clean_data(lines: list[str]) -> list[dict]:
    cats = []
    for line in lines:
        line = line.strip()
        if not line:
            continue

        try:
            cat_id, cat_name, cat_age = line.split(",")
            cat_info = {"id": cat_id, "name": cat_name, "age": cat_age}
            cats.append(cat_info)
        except ValueError:
            print(f"Некоректний рядок пропущено: {line}")

    return cats


def get_cats_info(path: str) -> list[dict]:
    try:
        lines = load_data(path)
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return []
    except UnicodeDecodeError:
        print(f"Файл пошкоджений або має неправильне кодування: {path}")
        return []

    return clean_data(lines)
