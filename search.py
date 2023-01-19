# Алгоритмы
# Поиск

from datetime import datetime

from utils import save_data_to_csv, get_data_from_csv


def get_first_or_last_occurrence(data: tuple, date: str, occurrence: str) -> int:
    """
        Возвращает индексы первого и последнего вхождения элемента по дате
    """

    date = datetime.strptime(date, '%Y-%m-%d')
    start = 0
    end = len(data) - 1
    index = 0

    while start <= end:
        mid = (start + end) // 2

        data_date = datetime.strptime(data[mid].get('date'), '%Y-%m-%d')

        if date == data_date:
            index = mid

            if occurrence == 'first':
                end = mid - 1
            else:
                start = mid + 1

        elif date < data_date:
            end = mid - 1
        else:
            start = mid + 1

    return index


def get_by_date(date: str, name: str) -> None:
    """
        Ищет записи по конкретной дате и конкретному имени, а затем сохраняет результат в csv-файл
    """

    data = get_data_from_csv('data/all_stocks_5yr_sorted_by_date.csv')
    data_result = ()

    first_occurrence = get_first_or_last_occurrence(data, date, 'first')
    last_occurrence = get_first_or_last_occurrence(data, date, 'last')

    for element in range(first_occurrence, last_occurrence+1):
        if data[element].get('Name') == name:
            data_result = (data[element], )

    if data_result:
        save_data_to_csv(data_result, 'search_result.csv')
    else:
        print('Данные не найдены.')

        save_data_to_csv(
            (
                {
                    'date': None,
                    'open': None,
                    'high': None,
                    'low': None,
                    'close': None,
                    'volume': None,
                    'Name': None
                },
            ),
            'search_result.csv'
        )
