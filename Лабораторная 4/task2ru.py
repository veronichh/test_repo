import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    """
    Читает CSV файл, конвертирует его в JSON и записывает в файл.
    """
    try:
        with open(INPUT_FILENAME, "r", newline="", encoding='utf-8') as csvfile:  # Добавлена обработка кодировки
            reader = csv.DictReader(csvfile)
            data = list(reader)

        with open(OUTPUT_FILENAME, "w", encoding='utf-8') as jsonfile:  # Добавлена обработка кодировки
            json.dump(data, jsonfile, indent=4)

    except FileNotFoundError:
        print(f"Файл {INPUT_FILENAME} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    # Создаем тестовый CSV файл с явным указанием кодировки UTF-8
    with open(INPUT_FILENAME, "w", newline="", encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms", "population", "households",
             "median_income", "median_house_value"])
        writer.writerow(["-122.050000", "37.370000", "27.000000", "3885.000000", "661.000000", "1537.000000", "606.000000", "6.608500", "344700.000000"])
        writer.writerow(["-118.300000", "34.260000", "43.000000", "1510.000000", "310.000000", "809.000000", "277.000000", "3.599000", "176500.000000"])
        writer.writerow(["-117.810000", "33.780000", "27.000000", "3589.000000", "507.000000", "1484.000000", "495.000000", "5.793400", "270500.000000"])
        writer.writerow(["-118.360000", "33.820000", "28.000000", "67.000000", "15.000000", "49.000000", "11.000000", "6.135900", "330000.000000"])

    task()

    with open(OUTPUT_FILENAME, encoding='utf-8') as output_f:  # Добавлена обработка кодировки
        for line in output_f:
            print(line, end="")