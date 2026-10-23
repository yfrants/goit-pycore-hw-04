from data import load_data, clean_data


def total_salary(path):
    try:
        lines = load_data(path)
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0
    except UnicodeDecodeError:
        print(f"Файл пошкоджений або має неправильне кодування: {path}")
        return 0, 0

    salaries = clean_data(lines)
    if not salaries:
        return 0, 0

    total = sum(salaries)
    average = int(total / len(salaries))

    return total, average
