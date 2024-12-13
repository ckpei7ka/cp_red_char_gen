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
            message_format="Твоя биография: {text}"
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
        if not(1 <= role_id <= 10):
            raise ValueError("Ваш класс не опознан")
        self.role_id = role_id

    def rockerboy_lifeway(self):
        def rockerboy_init():
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

        rockerboy_init()

  

    def solo_lifeway(self):
        def solo_init():
            solo_type()
            solo_morale()
            solo_work()
            solo_anthoganist()
        
        def solo_type():
            fetch_and_print_record(
                db_path=db_path,
                table_name="SOLO_TYPE",
                record_id=gend6(),
                fields=["text"],
                message_format="Какой вы Соло: {text}"
            )

        def solo_morale():
            fetch_and_print_record(
                db_path=db_path,
                table_name="SOLO_MORALE",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваш моральный кодекс: {text}"
            )

        def solo_work():
            fetch_and_print_record(
                db_path=db_path,
                table_name="SOLO_WORK",
                record_id=gend6(),
                fields=["text"],
                message_format="Вы обычно работаете в: {text}"
            )

        def solo_anthoganist():
            fetch_and_print_record(
                db_path=db_path,
                table_name="SOLO_ANTHOGANIST",
                record_id=gend6(),
                fields=["text"],
                message_format="За вами охотится: {text}"
            )
        
        solo_init()

    def netrunner_lifeway(self):
        def netrunner_init():
            netrunner_type()

            partner = randint(1,2)
            if partner < 2:
                print("Вы работаете в одиночку")
            else:
                print("Вы работаете не один")
                netrunner_partner()

            netrunner_workspace()
            netrunner_client()
            netrunner_program()
            netrunner_anthoganist()

        def netrunner_type():
            fetch_and_print_record(
                db_path=db_path,
                table_name="NETRUNNER_TYPE",
                record_id=gend6(),
                fields=["text"],
                message_format="Какой вы Нетраннер: {text}"
            )

        def netrunner_partner():
            fetch_and_print_record(
                db_path=db_path,
                table_name="NETRUNNER_PARTNER",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваш партнер: {text}"
            )

        def netrunner_workspace():
            fetch_and_print_record(
                db_path=db_path,
                table_name="NETRUNNER_WORKSPACE",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваше рабочее место: {text}"
            )

        def netrunner_client():
            fetch_and_print_record(
                db_path=db_path,
                table_name="NETRUNNER_CLIENT",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваши клиенты: {text}"
            )

        def netrunner_program():
            fetch_and_print_record(
                db_path=db_path,
                table_name="NETRUNNER_PROGRAM",
                record_id=gend6(),
                fields=["text"],
                message_format="Где вы берете свои программы: {text}"
            )

        def netrunner_anthoganist():
            fetch_and_print_record(
                db_path=db_path,
                table_name="NETRUNNER_ANTHOGANIST",
                record_id=gend6(),
                fields=["text"],
                message_format="За вами охотится: {text}"
            )
        
        netrunner_init()

    def tech_lifeway(self):
        def tech_init():
            tech_type()

            partner = randint(1,2)
            if partner < 2:
                print("Вы работаете в одиночку")
            else:
                print("Вы работете не один")
                tech_partner()

            tech_workspace()
            tech_client()
            tech_material()
            tech_anthoganist()

        def tech_type():
            fetch_and_print_record(
                db_path=db_path,
                table_name="TECH_TYPE",
                record_id=gend10(),
                fields=["text"],
                message_format="Какой вы Техник: {text}"
            )

        def tech_partner():
            fetch_and_print_record(
                db_path=db_path,
                table_name="TECH_PARTNER",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваш партнер: {text}"
            )

        def tech_workspace():
            fetch_and_print_record(
                db_path=db_path,
                table_name="TECH_WORKSPACE",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваше рабочее место: {text}"
            )

        def tech_client():
            fetch_and_print_record(
                db_path=db_path,
                table_name="TECH_CLIENT",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваши основные клиенты: {text}"
            )

        def tech_material():
            fetch_and_print_record(
                db_path=db_path,
                table_name="TECH_MATERIAL",
                record_id=gend6(),
                fields=["text"],
                message_format="Вы получаете материалы : {text}"
            )

        def tech_anthoganist():
            fetch_and_print_record(
                db_path=db_path,
                table_name="TECH_ANTHOGANIST",
                record_id=gend6(),
                fields=["text"],
                message_format="За вами охотится: {text}"
            )
        
        tech_init()

    def medtech_lifeway(self):
        def medtech_init():
            medtech_type()

            partner = randint(1,2)
            if partner < 2:
                print("Вы работаете в одиночку")
            else:
                print("Вы работаете не один")
                medtech_partner()
            
            medtech_workspace()
            medtech_client()
            medtech_material()
        
        def medtech_type():
            fetch_and_print_record(
                db_path=db_path,
                table_name="MEDTECH_TYPE",
                record_id=gend10(),
                fields=["text"],
                message_format="Какой вы Медтехник: {text}"
            )

        def medtech_partner():
            fetch_and_print_record(
                db_path=db_path,
                table_name="MEDTECH_PARTNER",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваш партнер: {text}"
            )

        def medtech_workspace():
            fetch_and_print_record(
                db_path=db_path,
                table_name="MEDTECH_WORKSPACE",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваше рабочее место: {text}"
            )

        def medtech_client():
            fetch_and_print_record(
                db_path=db_path,
                table_name="MEDTECH_CLIENT",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваши клиенты: {text}"
            )
        
        def medtech_material():
            fetch_and_print_record(
                db_path=db_path,
                table_name="MEDTECH_MATERIAL",
                record_id=gend6(),
                fields=["text"],
                message_format="Вы получаете материалы: {text}"
            )
        
        medtech_init()

    def media_lifeway(self):

        def media_init():
            media_type()
            media_publicity()
            media_ethic()
            media_story()
        
        def media_type():
            fetch_and_print_record(
                db_path=db_path,
                table_name="MEDIA_TYPE",
                record_id=gend6(),
                fields=["text"],
                message_format="Какой вы Медиа: {text}"
            )

        def media_publicity():
            fetch_and_print_record(
                db_path=db_path,
                table_name="MEDIA_PUBLICITY",
                record_id=gend6(),
                fields=["text"],
                message_format="Вы находите огласку: {text}"
            )

        def media_ethic():
            fetch_and_print_record(
                db_path=db_path,
                table_name="MEDIA_ETHICS",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваша этика: {text}"
            )
        
        def media_story():
            fetch_and_print_record(
                db_path=db_path,
                table_name="MEDIA_STORY",
                record_id=gend6(),
                fields=["text"],
                message_format="Вы рассказываете о: {text}"
            )
        
        media_init()

    def lowyer_lifeway(self):
        def lowyer_init():
            lowyer_type()
            lowyer_jurisdiction()
            lowyer_corrupt()
            lowyer_anthoganist()
            lowyer_target()
        
        def lowyer_type():
            fetch_and_print_record(
                db_path=db_path,
                table_name="LOWYER_TYPE",
                record_id=gend6(),
                fields=["text"],
                message_format="Какой вы Законник: {text}"
            )
        
        def lowyer_jurisdiction():
            fetch_and_print_record(
                db_path=db_path,
                table_name="LOWYER_JURISDICTION",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваша юрисдикция: {text}"
            )

        def lowyer_corrupt():
            fetch_and_print_record(
                db_path=db_path,
                table_name="LOWYER_CORRUPT",
                record_id=gend6(),
                fields=["text"],
                message_format="Насколько вы коррумпированы: {text}"
            )

        def lowyer_anthoganist():
            fetch_and_print_record(
                db_path=db_path,
                table_name="LOWYER_ANTHOGANIST",
                record_id=gend6(),
                fields=["text"],
                message_format="За вами охотится: {text}"
            )
        
        def lowyer_target():
            fetch_and_print_record(
                db_path=db_path,
                table_name="LOWYER_TARGET",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваша основная цель: {text}"
            )
        
        
        lowyer_init()

    def corp_lifeway(self):
        def corp_init():
            corp_type()
            corp_department()
            corp_goodbad()
            corp_where()
            corp_anthoganist()
            corp_boss()

        def corp_type():
            fetch_and_print_record(
                db_path=db_path,
                table_name="CORP_TYPE",
                record_id=gend10(),
                fields=["text"],
                message_format="Ваша компания занимается: {text}"
            )

        def corp_department():
             fetch_and_print_record(
                db_path=db_path,
                table_name="CORP_DEPARTMENT",
                record_id=gend6(),
                fields=["text"],
                message_format="Вы работаете в отделе: {text}"
            )

        def corp_goodbad():
             fetch_and_print_record(
                db_path=db_path,
                table_name="CORP_GOOD_BAD",
                record_id=gend6(),
                fields=["text"],
                message_format="Насколько хороша/плоха ваша корпа: {text}"
            )

        def corp_where():
             fetch_and_print_record(
                db_path=db_path,
                table_name="CORP_WHERE",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваша корпа находится: {text}"
            )

        def corp_anthoganist():
             fetch_and_print_record(
                db_path=db_path,
                table_name="CORP_ANTHOGANIST",
                record_id=gend6(),
                fields=["text"],
                message_format="За вами охотится: {text}"
            )

        def corp_boss():
             fetch_and_print_record(
                db_path=db_path,
                table_name="CORP_BOSS",
                record_id=gend6(),
                fields=["text"],
                message_format="Отношения с вашим босом: {text}"
            )

        corp_init()

    def nomad_lifeway(self):
        def nomad_init():
            nomad_swarm()
            nomad_based_on()
            nomad_type()
            nomad_philosophy()
            nomad_anthoganist()
        
        def nomad_based_on():
            match gend6() / 2:
                case 1:
                    print("Ваша стая базируется на земле")
                    nomad_land()
                case 2:
                    print("Ваша стая базируется в воздухе")
                    nomad_air()
                case 3:
                    print("Ваша стая базируется в море")
                    nomad_ocean()


        def nomad_swarm():
            fetch_and_print_record(
                db_path=db_path,
                table_name="NOMAD_SWARM",
                record_id=gend6(),
                fields=["text"],
                message_format="Размер вашей стаи: {text}"
            )
        
        def nomad_land():
            fetch_and_print_record(
                db_path=db_path,
                table_name="NOMAD_LAND",
                record_id=gend10(),
                fields=["text"],
                message_format="На суше ваша стая занимается: {text}"
            )
        
        def nomad_air():
            fetch_and_print_record(
                db_path=db_path,
                table_name="NOMAD_AIR",
                record_id=gend6(),
                fields=["text"],
                message_format="В воздухе ваша стая занимается: {text}"
            )

        def nomad_ocean():
            fetch_and_print_record(
                db_path=db_path,
                table_name="NOMAD_OCEAN",
                record_id=gend6(),
                fields=["text"],
                message_format="В море ваша стая занимается: {text}"
            )

        def nomad_type():
            fetch_and_print_record(
                db_path=db_path,
                table_name="NOMAD_TYPE",
                record_id=gend6(),
                fields=["text"],
                message_format="Для клана вы занимаетесь: {text}"
            )

        def nomad_philosophy():
            fetch_and_print_record(
                db_path=db_path,
                table_name="NOMAD_PHILOSOPHY",
                record_id=gend6(),
                fields=["text"],
                message_format="Философия вашей стаи: {text}"
            )
        def nomad_anthoganist():
            fetch_and_print_record(
                db_path=db_path,
                table_name="NOMAD_ANTHOGANIST",
                record_id=gend6(),
                fields=["text"],
                message_format="За вами охотится: {text}"
            )
        
        nomad_init()

    def fixer_lifeway(self):
        def fixer_init():
            fixer_type()
            partner = randint(1,2)
            if partner < 2:
                print("Вы работаете в одиночку")
            else:
                print("Вы работаете не один")
                fixer_partner()
            fixer_office()
            fixer_client()
            fixer_anthoganist()

        def fixer_type():
            fetch_and_print_record(
                db_path=db_path,
                table_name="FIXER_TYPE",
                record_id=gend10(),
                fields=["text"],
                message_format="Какой вы Фиксер: {text}"
            )

        def fixer_partner():
            fetch_and_print_record(
                db_path=db_path,
                table_name="FIXER_PARTNER",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваш партнер: {text}"
            )

        def fixer_office():
            fetch_and_print_record(
                db_path=db_path,
                table_name="FIXER_OFFICE",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваш офис: {text}"
            )

        def fixer_client():
            fetch_and_print_record(
                db_path=db_path,
                table_name="FIXER_CLIENT",
                record_id=gend6(),
                fields=["text"],
                message_format="Ваши клиенты: {text}"
            )

        def fixer_anthoganist():
            fetch_and_print_record(
                db_path=db_path,
                table_name="FIXER_ANTHOGANIST",
                record_id=gend6(),
                fields=["text"],
                message_format="За вами охотится: {text}"
            )

        fixer_init()

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
            10: self.fixer_lifeway,
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
        record_id=gend10(),
        fields=["text"],
        message_format="Твоя роль:{text}"
    )

    LifeWayCommon.__init__(db_path=db_path)
    role_instance = LifeWayRole(role_id)
    role_instance.generate_text()
