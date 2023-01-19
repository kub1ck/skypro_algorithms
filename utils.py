import csv
import json


def get_data_from_csv(filename: str) -> tuple:
    """
        Возвращает данные из csv-файла
    """

    with open(filename, encoding='utf-8') as file:
        return tuple(csv.DictReader(file))


def get_data_from_json(filename: str) -> dict:
    """
        Возвращает данные из json-файла
    """

    with open(filename) as file:
        return json.load(file)


def save_data_to_csv(data: tuple, filename: str) -> None:
    """
        Сохраняет данные в csv-файл
    """

    fields = data[0].keys()

    with open(f'result/{filename}', 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        for line in data:
            writer.writerow(line)


def save_data_to_json(data: dict) -> None:
    """
        Сохраняет данные в хеш-таблицу
    """

    with open('data/hash_table.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)


def show_data(filename: str) -> None:
    """
        Выводит данные в консоль
    """

    with open(f'result/{filename}', encoding='utf-8') as file:
        data = tuple(csv.DictReader(file))

        for i, line in enumerate(data):
            print(
                f"\nЗапись №{i+1}\n"
                f"Дата: {line.get('date')}\n"
                f"Цена акции при открытии рынка: {line.get('open')}\n"
                f"Самая высокая цена за день: {line.get('high')}\n"
                f"Самая низкая цена за день: {line.get('low')}\n"
                f"Цена акции при закрытии рынка: {line.get('close')}\n"
                f"Кол-во проданных акций: {line.get('volume')}\n"
                f"Название тикера акции: {line.get('Name')}"
            )
