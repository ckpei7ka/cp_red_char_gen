import sqlite3
from random import randint, choice
import lifepath_common
import lifepath_class


def gend6():
    random_number = randint(1, 6)
    return random_number

def gend10():
    random_number = randint(1, 10)
    return random_number

def get_and_print_record(db_path, table_name, record_id, fields, message_format):
    """
    Получает значения нескольких полей из указанной таблицы SQLite на основе идентификатора
    и выводит результат в заданном формате.

    :param db_path: Путь к базе данных SQLite.
    :param table_name: Имя таблицы для извлечения данных.
    :param record_id: Идентификатор записи.
    :param fields: Список полей, которые нужно извлечь.
    :param message_format: Форматированный текст с плейсхолдерами вида {field}.
    :return: Значение record_id при успешном выполнении или None, если запись не найдена.
    """
    # Формируем SQL-запрос
    fields_str = ", ".join(fields)
    query = f"SELECT {fields_str} FROM {table_name} WHERE id = ?"

    try:
        # Подключаемся к базе данных
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Выполняем SQL-запрос
        cursor.execute(query, (record_id,))
        result = cursor.fetchone()

        # Проверка на наличие данных
        if result:
            record = dict(zip(fields, result))
            print(message_format.format(**record))  # Выводим форматированные данные
            return record_id  # Возвращаем record_id при успешном нахождении записи
        else:
            print(f"Запись с id {record_id} не найдена в таблице {table_name}.")
            return None

    except sqlite3.Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

    finally:
        # Закрываем курсор и соединение
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    db_path = "app/db/database.db"
    role_id = get_and_print_record(db_path=db_path,
        table_name="ROLE",
        record_id=gend10(),
        fields=["text"],
        message_format="Твоя роль:{text}"
    )
    lifeway_common = lifepath_common.__init__(db_path)
    lifeway_class = lifepath_class.init(role_id, db_path)