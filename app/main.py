import sqlite3
from random import randint, choice

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
    return record_id

### Функции для генерации жизненого пути

class LifeWayCommon:

    def __init__(db_path):
        db_path = db_path
        region_name, languages = LifeWayCommon.get_region_and_languages(db_path)
        LifeWayCommon.cultural_origin(region_name=region_name, languages=languages)  # Выбор культурного происхождения и языка
        LifeWayCommon.self_identity()       # Выбор личности
        LifeWayCommon.outfit_and_style()    # Выбор одежды и стиля
        LifeWayCommon.hairstyle()           # Выбор прически
        LifeWayCommon.addictions()          # Выбор без чего вы не появляетесь
        LifeWayCommon.self_value()          # Выбор что для вас ценнее всего
        LifeWayCommon.feel_majority()       # Выбор отношения к большенству людей 
        LifeWayCommon.closest_person()      # Выбор самого близкого человека
        LifeWayCommon.valuable_thing()      # Выбор самого ценного, чем вы обладаете
        LifeWayCommon.how_did_you_life()    # Выбор вашего семейного прошлого
        LifeWayCommon.childhood()           # Выбор вашего детства
        LifeWayCommon.biography()           # Выбор биографии
        LifeWayCommon.friends()             # Выбор ваших друзей
        LifeWayCommon.enemies()             # Выбор ваших врагов
        LifeWayCommon.tragic_romance()      # Выбор ваших трагических романов
        LifeWayCommon.life_goal()           # Выбор вашей цели в жизни
        
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
    def self_identity():
        fetch_and_print_record(
            db_path=db_path,
            table_name="SELF_IDENTITY",
            record_id=gend10(),
            fields=["text"],
            message_format="Вы представляете из себя: {text}"
        )    

    # Одежда и личный стиль
    def outfit_and_style():
        fetch_and_print_record(
            db_path=db_path,
            table_name="OUTFIT_AND_STYLE",
            record_id=gend10(),
            fields=["text"],
            message_format="Твой стиль: {text}"
        )
    # Прическа
    def hairstyle():
        fetch_and_print_record(
            db_path=db_path,
            table_name="HAIRSTYLE",
            record_id=gend10(),
            fields=["text"],
            message_format="Твоя прическа: {text}"
        )

    # Пристрастия, без которых вы не появляетесь
    def addictions():
        fetch_and_print_record(
            db_path=db_path,
            table_name="ADDICTIONS",
            record_id=gend10(),
            fields=["text"],
            message_format="Вы не выходите без: {text}"
        )

    # Что для вас ценнее всего
    def self_value():
        fetch_and_print_record(
            db_path=db_path,
            table_name="SELF_VALUE",
            record_id=gend10(),
            fields=["text"],
            message_format="Для тебя ценнее всего: {text}"
        )
    
    # Отношение к большинству
    def feel_majority():
        fetch_and_print_record(
            db_path=db_path,
            table_name="FEEL_MAJORITY",
            record_id=gend10(),
            fields=["text"],
            message_format="Твое отношение к большинству людей: {text}"
        )

    # Самый близкий человек в жизни
    def closest_person():
        fetch_and_print_record(
            db_path=db_path,
            table_name="CLOSEST_PERSON",
            record_id=gend10(),
            fields=["text"],
            message_format="Твой самый близкий человек в жизни: {text}"
        )

    # Самое ценное, чем вы обладаете
    def valuable_thing():
        fetch_and_print_record(
            db_path=db_path,
            table_name="VALUABLE_THING",
            record_id=gend10(),
            fields=["text"],
            message_format="Самое ценное, чем вы обладаете: {text}"
        )

    # Ваше семейное прошлое
    def how_did_you_life():
        fetch_and_print_record(
            db_path=db_path,
            table_name="HOW_DID_YOU_LIFE",
            record_id=gend10(),
            fields=["text", "discription"],
            message_format="Семейное прошлое: {text} \nОписание прошлого: {discription}"
        )

    # Ваше детство
    def childhood():
        fetch_and_print_record(
            db_path=db_path,
            table_name="CHILDHOOD",
            record_id=gend10(),
            fields=["text"],
            message_format="Твое детство: {text}"
        )

    # Биография
    def biography():
        fetch_and_print_record(
            db_path=db_path,
            table_name="BIOGRAPHY",
            record_id=gend10(),
            fields=["text"],
            message_format="Твой биография: {text}"
        )

    # Ваши друзья
    def friends():
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
    def enemies():
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
    def tragic_romance():
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
    def life_goal():
        fetch_and_print_record(
            db_path=db_path,
            table_name="LIFE_GOAL",
            record_id=gend10(),
            fields=["text"],
            message_format="Твоя жизненная цель: {text}"
        )

class LifeWayRole:
    def __init__(self, role_id):
        if not(1 <= role_id <= 9):
            raise ValueError("Ваш класс не опознан")
        self.role_id = role_id

    def rockerboy_lifeway(self):

        def rockerboy_type():
            fetch_and_print_record(
                db_path=db_path,
                table_name="ROCKERBOY_TYPE",
                record_id=gend10(),
                fields=["text"],
                message_format="Какой вы Рокеробой: {text}"
            )

        def rockerboy_group_collapse():
            fetch_and_print_record(
                db_path=db_path,
                table_name="ROCKERBOY_GROUP_COLLAPSE",
                record_id=gend6(),
                fields=["text"],
                message_format="Вы ушли из группы из-за: {text}"
            )

        def rockerboy_where_perform():
            fetch_and_print_record(
                db_path=db_path,
                table_name="ROCKERBOY_WHERE_PERFORM",
                record_id=gend6(),
                fields=["text"],
                message_format="Вы выступаете: {text}"
            )

        def rockerboy_anthoganist():
            fetch_and_print_record(
                db_path=db_path,
                table_name="ROCKERBOY_ANTHOGANIST",
                record_id=gend6(),
                fields=["text"],
                message_format="За вами охотится: {text}"
            )

        rockerboy_type()
        group_or_solo = randint(1,2)
        if group_or_solo < 2:
            print("Ты выступаешь один")
            group_before = randint(1,2)
            if group_before < 2:
                print("Раньше ты выступал в группе")
                rockerboy_group_collapse()               
            else:
                print("Ты выступаешь почти всегда один")
                rockerboy_where_perform()
        else:
            print("Ты выступаешь в группе")
            rockerboy_where_perform()

        rockerboy_anthoganist()

  

    def solo_lifeway(self):
        return("Твоя роль: Соло")

    def netrunner_lifeway(self):
        return("Твоя роль: Нетраннер")

    def tech_lifeway(self):
        return("Твоя роль: Техник")

    def medtech_lifeway(self):
        return("Твоя роль: Медтехник")

    def media_lifeway(self):
        return("Твоя роль: Медиа")

    def lowyer_lifeway(self):
        return("Твоя роль: Законник")

    def corp_lifeway(self):
        return("Твоя роль: Корпорат")

    def nomad_lifeway(self):
        return("Твоя роль: Кочевник")
    
    def generate_text(self):
        # Сопоставление role_id с методом обработки
        lifeway_method = {
            1: self.rockerboy_lifeway,
            2: self.solo_lifeway,
            3: self.netrunner_lifeway,
            4: self.tech_lifeway,
            5: self.medtech_lifeway,
            6: self.media_lifeway,
            7: self.lowyer_lifeway,
            8: self.corp_lifeway,
            9: self.nomad_lifeway,
        }

        method = lifeway_method.get(self.role_id)
        if method:
            return method()
        else:
            raise ValueError("Ваш класс не определен")
        

if __name__ == "__main__":
    role_id = fetch_and_print_record(
        db_path=db_path,
        table_name="ROLE",
        record_id=randint(1,9),
        fields=["text"],
        message_format="Твоя роль:{text}"
    )

    LifeWayCommon.__init__(db_path=db_path)
    role_instance = LifeWayRole(role_id)
    print(role_instance.generate_text())
