import json
import os


# Сохраняет данные в JSON-файл
def save_data(data: list, filename: str) -> None:
    # Создаем папку data, если её нет
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Загружает данные из JSON-файла. Если файла нет, возвращает пустой список
def load_data(filename: str) -> list:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        # Если файл поврежден или пуст
        return []
