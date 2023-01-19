# Алгоритмы
# Сортировка

from utils import get_data_from_csv, save_data_to_csv


def select_sorted(sort_columns: list, limit: int, order: str, filename: str) -> None:
    """
        Сортирует данные, а затем сохраняет результат в csv-файл
    """

    data = get_data_from_csv("data/all_stocks_5yr.csv")
    is_reverse = True if order == 'desc' else False

    # Сортировка по колонкам
    for column in sort_columns:
        data = sorted(data, key=lambda x: x.get(column), reverse=is_reverse)

    save_data_to_csv(data[:limit], filename)
