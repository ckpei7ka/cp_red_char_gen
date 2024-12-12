import sqlite3
from random import randint

db_path = "app/db/database.db"

def gend6():
    random_number = randint(1, 6)
    return random_number

def gend10():
    random_number = randint(1, 10)
    return random_number

def get_record_by_id(db_path, table_name, record_id, fields):
    """
    Получает значения нескольких полей из указанной таблицы
    на основе переданного идентификатора.

    :param db_path: Строка пути к базе данных SQLite.
    :param table_name: Имя таблицы, из которой нужно получить данные.
    :param record_id: Идентификатор записи.
    :param fields: Список полей, которые нужно извлечь.
    :return: Словарь с именами полей и их значениями, или None, если запись не найдена.
    """
    # Формирование строки запроса с полями, указанными в `fields`
    fields_str = ", ".join(fields)
    query = f"SELECT {fields_str} FROM {table_name} WHERE id = ?"

    try:
        # Подключение к базе данных
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        
        # Выполнение SQL-запроса
        cursor.execute(query, (record_id,))
        result = cursor.fetchone()
        
        # Если запись найдена, создаем словарь вида {<field>: <value>}
        if result:
            return dict(zip(fields, result))
        else:
            return None  # Запись не найдена

    except sqlite3.Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

    finally:
        # Закрытие соединения
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def fetch_and_print_record(db_path, table_name, record_id, fields, message_format):
    """
    Универсальная функция для получения нескольких значений полей и
    вывода результата в форматированном виде.

    :param db_path: Строка пути к базе данных SQLite.
    :param table_name: Имя таблицы, из которой нужно извлечь данные.
    :param record_id: Идентификатор записи.
    :param fields: Список полей, которые нужно получить.
    :param message_format: Формат сообщения с плейсхолдерами вида `{field}`.
    """
    record = get_record_by_id(db_path, table_name, record_id, fields)
    
    # Если запись найдена, выводим ее в заданном формате
    if record:
        print(message_format.format(**record))
    else:
        print(f"Запись с id {record_id} не найдена в таблице {table_name}.")

def get_region_and_languages(db_path):
    """
    Извлекает имя региона и связанные с ним языки
    на основе заданного SQL-запроса
    """
    # Путь к SQLite базе данных
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    try:
        # Получение случайного id для случайного региона
        random_id = gend10()

        # Запрос к базе данных, с выборкой имени региона и языков
        sql_query = """
        SELECT 
            CULT_BACK.text AS region_name,    -- Имя региона
            LANG.text AS language_name       -- Имя языка
        FROM 
            REGION_LANGUAGES
        JOIN 
            CULT_BACK ON REGION_LANGUAGES.region_id = CULT_BACK.id
        JOIN 
            LANG ON REGION_LANGUAGES.language_id = LANG.id
        WHERE 
            CULT_BACK.id = ?
        ORDER BY 
            CULT_BACK.text, LANG.text;
        """
        cursor.execute(sql_query, (random_id,))
        results = cursor.fetchall()

        # Если есть данные
        if results:
            # Получение имени региона
            region_name = results[0][0]
            
            # Список языков
            language_names = [row[1] for row in results]

            return region_name, language_names
        else:
            return None, None

    except sqlite3.Error as e:
        print(f"Ошибка: {e}")
        return None, None

    finally:
        cursor.close()
        connection.close()

def life_way_common():
    # Культурное происхождение
    if LifeWayGen.region_name:
        print(f"Культурное происхождение: {LifeWayGen.region_name}")
        print(f"Языки региона: {','.join(LifeWayGen.languages)}")
    else:
        print("Запись с указанным id не найдена.")
    
    # Ваша личность
    fetch_and_print_record(
        db_path=db_path,
        table_name="SELF_IDENTITY",
        record_id=gend10(),
        fields=["text"],
        message_format="Вы представляете из себя: {text}"
    )

    # Одежда и личный стиль
    fetch_and_print_record(
        db_path=db_path,
        table_name="OUTFIT_AND_STYLE",
        record_id=gend10(),
        fields=["text"],
        message_format="Твой стиль: {text}"
    )

    # Прическа
    fetch_and_print_record(
        db_path=db_path,
        table_name="HAIRSTYLE",
        record_id=gend10(),
        fields=["text"],
        message_format="Твоя прическа: {text}"
    )
    
    # Пристрастия, без которых вы не появляетесь
    fetch_and_print_record(
        db_path=db_path,
        table_name="ADDICTIONS",
        record_id=gend10(),
        fields=["text"],
        message_format="Вы не выходите без: {text}"
    )

    # Что для вас ценнее всего
    fetch_and_print_record(
        db_path=db_path,
        table_name="SELF_VALUE",
        record_id=gend10(),
        fields=["text"],
        message_format="Для тебя ценнее всего: {text}"
    )

    # Ваше отношение к большинству людей
    fetch_and_print_record(
        db_path=db_path,
        table_name="FEEL_MAJORITY",
        record_id=gend10(),
        fields=["text"],
        message_format="Твое отношение к большинству людей: {text}"
    )

    # Самый близкий человек в жизни
    fetch_and_print_record(
        db_path=db_path,
        table_name="CLOSEST_PERSON",
        record_id=gend10(),
        fields=["text"],
        message_format="Твой самый близкий человек в жизни: {text}"
    )

    # Самое ценное, чем вы обладаете
    fetch_and_print_record(
        db_path=db_path,
        table_name="VALUABLE_THING",
        record_id=gend10(),
        fields=["text"],
        message_format="Самое ценное, чем вы обладаете: {text}"
    )

    # Ваше семейное прошлое
    fetch_and_print_record(
        db_path=db_path,
        table_name="HOW_DID_YOU_LIFE",
        record_id=gend10(),
        fields=["text", "discription"],
        message_format="Семейное прошлое: {text}, , \nОписание прошлого: {discription}"
    )

    # Ваше детство
    fetch_and_print_record(
        db_path=db_path,
        table_name="CHILDHOOD",
        record_id=gend10(),
        fields=["text"],
        message_format="Твое детство: {text}"
    )

    # Биография
    fetch_and_print_record(
        db_path=db_path,
        table_name="BIOGRAPHY",
        record_id=gend10(),
        fields=["text"],
        message_format="Твой биография: {text}"
    )

    # Ваши друзья
    num_friend = gend10() - 7
    if num_friend > 0:
        print(f"Вы считаете, что у вас {num_friend} друзей")
        for i in range(num_friend):
            fetch_and_print_record(
                db_path=db_path,
                table_name="FRIEND_WHO",
                record_id=gend10(),
                fields=["text"],
                message_format="Твой друг: {text}"
    )
    else:
        print("Вы считаете, что у вас нет друзей")

    # Ваши враги
    num_enemy = gend10() - 7
    if num_enemy > 0:
        print(f"Вы считаете, что у вас {num_enemy} врагов")
        for i in range(num_enemy):
            # Кто твой враг
            fetch_and_print_record(
                db_path=db_path,
                table_name="ENEMY_WHO",
                record_id=gend10(),
                fields=["text"],
                message_format="Твой враг: {text}"
            )
            # Что послужило причиной? Кто был обижен
            fetch_and_print_record(
                db_path=db_path,
                table_name="ENEMY_REASON",
                record_id=gend10(),
                fields=["text"],
                message_format="Причина вражды: {text}"
            )
            # Как они могут напасть на вас?
            fetch_and_print_record(
                db_path=db_path,
                table_name="ENEMY_WHO",
                record_id=gend10(),
                fields=["attack"],
                message_format="Они могут напасть на вас: {attack}"
            )
            # Что вы/они собираетесь делать
            fetch_and_print_record(
                db_path=db_path,
                table_name="ENEMY_REVENGE",
                record_id=gend10(),
                fields=["text"],
                message_format="Что вы/они собираетесь делать: {text}"
            )

    else:
        print("Вы считаете, что у вас нет врагов")

    # Ваш трагический роман
    num_tragic_romance = gend10() - 7
    if num_tragic_romance > 0:
        print(f"Вы считаете, что у вас {num_tragic_romance} трагических романов")
        for i in range(num_tragic_romance):
            fetch_and_print_record(
                db_path=db_path,
                table_name="TRAGIC_ROMANCE",
                record_id=gend10(),
                fields=["text"],
                message_format="Твой трагический роман: {text}"
    )
    else:
        print("Вы считаете, что у вас нет трагических романов ")

    # Ваша цель всей жизни
    fetch_and_print_record(
        db_path=db_path,
        table_name="LIFE_GOAL",
        record_id=gend10(),
        fields=["text"],
        message_format="Твоя жизненная цель: {text}"
    )

class LifeWayGen:
    region_name, languages = get_region_and_languages(db_path)
    


if __name__ == "__main__":
    life_way_common()
