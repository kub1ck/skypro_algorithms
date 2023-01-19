# Алгоритмы
# Хеш-таблицы

from utils import save_data_to_json, get_data_from_json


def hash_function(key: str) -> int:
    """
        Формирует хеш-значение, а затем возвращает его
    """

    hash_value = 0
    table_size = 100

    for symbol in key:
        hash_value += ord(symbol)

    hash_value %= table_size

    return hash_value


def get_value_from_hash_table(sort_columns: list, order: str, limit: int, filename: str) -> str:
    """
         Проверяет, имеется ли результат в кэше, а затем возвращает его
    """

    key = ''.join(sort_columns) + order + str(limit)
    hash_key = str(hash_function(key))
    hash_table = get_data_from_json("data/hash_table.json")

    if hash_key not in hash_table:
        hash_table[hash_key] = filename
        save_data_to_json(hash_table)

        return ''

    return hash_table[hash_key]
