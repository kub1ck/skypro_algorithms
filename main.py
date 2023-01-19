from shutil import copyfile
from os.path import abspath

from hash import get_value_from_hash_table
from utils import show_data
from sort import select_sorted
from search import get_by_date


def sort_(is_hash: bool = False) -> None:
    """
        Запуск сортировки без хеш-таблицы или вместе с ней
    """

    print("\nВведите колонки для сортировки")
    sort_columns = input("Колонки: ").split()

    print("\nСколько записей нужно сохранить?")
    limit = int(input("Кол-во записей: "))

    print("\nСортировка по убыванию(desc) или возрастанию(asc)?")
    order = input("Сортировка: ")

    print("\nВведите имя файла для сохранения")
    filename = input("Имя файла: ") + '.csv'

    if not is_hash:
        select_sorted(sort_columns, limit, order, filename)
        show_data(filename)
    else:
        filename_from_hash = get_value_from_hash_table(sort_columns, order, limit, filename)

        if not filename_from_hash:
            select_sorted(sort_columns, limit, order, filename)
        else:
            # Если данные хранятся в кеше, то файл просто скопируется
            copyfile(abspath(f'result/{filename_from_hash}'), abspath(f'result/{filename}'))

        filename_from_hash = filename
        show_data(filename_from_hash)


def search_() -> None:
    """
        Запуск поиска
    """

    print("\nВведите дату для поиска (yyyy-mm-dd)")
    date = input("дата: ")

    print("\nВведите имя тикера акции")
    name = input("Имя: ")

    print("\nВведите имя файла для сохранения")
    filename = input("Имя файла: ") + '.csv'

    get_by_date(date, name)
    show_data(filename)


def main() -> None:
    while True:
        print('\n1 - сортировать данные;',
              '2 - поиск по дату и имени;',
              '3 - сортировать данные с использование хеш-таблицы;',
              'Любой другой символ - выйти из программы',
              sep='\n')

        user_choice = input("\nВаш выбор: ")

        match user_choice:
            case '1':
                sort_()
            case '2':
                search_()
            case '3':
                sort_(is_hash=True)
            case _:
                break


if __name__ == '__main__':
    main()
