
import json

def task() -> float:
    """
    Читает JSON файл, вычисляет произведение 'score' * 'weight' для каждого словаря
    и возвращает сумму этих произведений, округленную до 3 знаков после запятой.
    """
    try:
        with open("input.json", "r") as file: # Предполагается, что файл называется input.json.
            data = json.load(file)
    except FileNotFoundError:
        print("Файл input.json не найден.")
        return 0.0
    except json.JSONDecodeError:
        print("Ошибка при чтении JSON файла. Возможно, некорректный JSON.")
        return 0.0

    total_sum = 0
    for item in data: # Исправлено: data уже является списком словарей
        try:
            score = item["score"]
            weight = item["weight"]
            total_sum += score * weight
        except KeyError:
            print("В одном из словарей отсутствуют ключи 'score' или 'weight'.")


    return round(total_sum, 3)


print(task())