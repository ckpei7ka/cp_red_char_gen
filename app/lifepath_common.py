import sqlite3
from random import randint, choice


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

def __init__(db_path=None):  # Конструктор с дефолтным значением db_path
    # Если db_path не передан, используем значение по умолчанию
    db_path = db_path or "app/db/database.db"
    
    # Вызываем нужные методы с переданными или обработанными данными
    region_name, languages = get_region_and_languages(db_path)
    cultural_origin(region_name=region_name, languages=languages)  # Выбор культурного происхождения и языка
    _identity(db_path)           # Выбор личности
    outfit_and_style(db_path)    # Выбор одежды и стиля
    hairstyle(db_path)           # Выбор прически
    addictions(db_path)          # Выбор без чего вы не появляетесь
    _value(db_path)              # Выбор что для вас ценнее всего
    feel_majority(db_path)       # Выбор отношения к большинству людей 
    closest_person(db_path)      # Выбор самого близкого человека
    valuable_thing(db_path)      # Выбор самого ценного, чем вы обладаете
    how_did_you_life(db_path)    # Выбор вашего семейного прошлого
    childhood(db_path)           # Выбор вашего детства
    biography(db_path)           # Выбор биографии
    friends(db_path)             # Выбор ваших друзей
    enemies(db_path)             # Выбор ваших врагов
    tragic_romance(db_path)      # Выбор ваших трагических романов
    life_goal(db_path)           # Выбор вашей цели в жизни

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

# Культурное происхождение
def cultural_origin(region_name, languages):
    if region_name:
        print(f"Культурное происхождение: {region_name}")
        chosen_language = choice(languages)
        print(f"Ваш язык: {chosen_language}")
    else:
        print("Ваш регион не найден.")

# Ваша личность
def _identity(db_path):
    get_and_print_record(
        db_path=db_path,
        table_name="SELF_IDENTITY",
        record_id=gend10(),
        fields=["text"],
        message_format="Вы представляете из себя: {text}"
    )    

# Одежда и личный стиль
def outfit_and_style(db_path):
    get_and_print_record(
        db_path=db_path,
        table_name="OUTFIT_AND_STYLE",
        record_id=gend10(),
        fields=["text"],
        message_format="Твой стиль: {text}"
    )
# Прическа
def hairstyle(db_path):
    get_and_print_record(
        db_path=db_path,
        table_name="HAIRSTYLE",
        record_id=gend10(),
        fields=["text"],
        message_format="Твоя прическа: {text}"
    )

# Пристрастия, без которых вы не появляетесь
def addictions(db_path):
    get_and_print_record(
        db_path=db_path,
        table_name="ADDICTIONS",
        record_id=gend10(),
        fields=["text"],
        message_format="Вы не выходите без: {text}"
    )

# Что для вас ценнее всего
def _value(db_path):
    get_and_print_record(
        db_path=db_path,
        table_name="SELF_VALUE",
        record_id=gend10(),
        fields=["text"],
        message_format="Для тебя ценнее всего: {text}"
    )

# Отношение к большинству
def feel_majority(db_path):
    get_and_print_record(
        db_path=db_path,
        table_name="FEEL_MAJORITY",
        record_id=gend10(),
        fields=["text"],
        message_format="Твое отношение к большинству людей: {text}"
    )

# Самый близкий человек в жизни
def closest_person(db_path):
    get_and_print_record(
        db_path=db_path,
        table_name="CLOSEST_PERSON",
        record_id=gend10(),
        fields=["text"],
        message_format="Твой самый близкий человек в жизни: {text}"
    )

# Самое ценное, чем вы обладаете
def valuable_thing(db_path):
    get_and_print_record(
        db_path=db_path,
        table_name="VALUABLE_THING",
        record_id=gend10(),
        fields=["text"],
        message_format="Самое ценное, чем вы обладаете: {text}"
    )

# Ваше семейное прошлое
def how_did_you_life(db_path):
    get_and_print_record(
        db_path=db_path,
        table_name="HOW_DID_YOU_LIFE",
        record_id=gend10(),
        fields=["text", "discription"],
        message_format="Семейное прошлое: {text} \nОписание прошлого: {discription}"
    )

# Ваше детство
def childhood(db_path):
    get_and_print_record(
        db_path=db_path,
        table_name="CHILDHOOD",
        record_id=gend10(),
        fields=["text"],
        message_format="Твое детство: {text}"
    )

# Биография
def biography(db_path):
    get_and_print_record(
        db_path=db_path,
        table_name="BIOGRAPHY",
        record_id=gend10(),
        fields=["text"],
        message_format="Твоя биография: {text}"
    )

# Ваши друзья
def friends(db_path):
    num_friend = gend10() - 7
    if num_friend > 0:
        print(f"Вы считаете, что у вас {num_friend} друзей")
        for i in range(num_friend):
            get_and_print_record(
                db_path=db_path,
                table_name="FRIEND_WHO",
                record_id=gend10(),
                fields=["text"],
                message_format="Твой друг: {text}"
    )
    else:
        print("Вы считаете, что у вас нет друзей")

# Ваши враги
def enemies(db_path):
    num_enemy = gend10() - 7
    if num_enemy > 0:
        print(f"Вы считаете, что у вас {num_enemy} врагов")
        for i in range(num_enemy):
            # Кто твой враг
            get_and_print_record(
                db_path=db_path,
                table_name="ENEMY_WHO",
                record_id=gend10(),
                fields=["text"],
                message_format="Твой враг: {text}"
            )
            # Что послужило причиной? Кто был обижен
            get_and_print_record(
                db_path=db_path,
                table_name="ENEMY_REASON",
                record_id=gend10(),
                fields=["text"],
                message_format="Причина вражды: {text}"
            )
            # Как они могут напасть на вас?
            get_and_print_record(
                db_path=db_path,
                table_name="ENEMY_WHO",
                record_id=gend10(),
                fields=["attack"],
                message_format="Они могут напасть на вас: {attack}"
            )
            # Что вы/они собираетесь делать
            get_and_print_record(
                db_path=db_path,
                table_name="ENEMY_REVENGE",
                record_id=gend10(),
                fields=["text"],
                message_format="Что вы/они собираетесь делать: {text}"
            )

    else:
        print("Вы считаете, что у вас нет врагов")

# Ваш трагический роман
def tragic_romance(db_path):
    num_tragic_romance = gend10() - 7
    if num_tragic_romance > 0:
        print(f"Вы считаете, что у вас {num_tragic_romance} трагических романов")
        for i in range(num_tragic_romance):
            get_and_print_record(
                db_path=db_path,
                table_name="TRAGIC_ROMANCE",
                record_id=gend10(),
                fields=["text"],
                message_format="Твой трагический роман: {text}"
    )
    else:
        print("Вы считаете, что у вас нет трагических романов ")

# Ваша цель всей жизни
def life_goal(db_path):
    get_and_print_record(
        db_path=db_path,
        table_name="LIFE_GOAL",
        record_id=gend10(),
        fields=["text"],
        message_format="Твоя жизненная цель: {text}"
    )