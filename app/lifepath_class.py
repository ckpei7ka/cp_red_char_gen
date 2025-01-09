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


def init(role_id, db_path=None):
    """
    Инициализирующая функция для выбора метода lifeway в зависимости от role_id.

    :param role_id: Идентификатор роли игрока (int)
    :param db_path: Путь к базе данных (опционально)
    :return: Результат вызванного метода lifeway
    """
    db_path = db_path or "app/db/database.db"

    # Сопоставление role_id с методом обработки
    lifeway_method = {
        1: rockerboy_lifeway,
        2: solo_lifeway,
        3: netrunner_lifeway,
        4: tech_lifeway,
        5: medtech_lifeway,
        6: media_lifeway,
        7: lowyer_lifeway,
        8: corp_lifeway,
        9: nomad_lifeway,
        10: fixer_lifeway,
    }

    method = lifeway_method.get(role_id)
    if method:
        # Возврат метода lifeway
        return method(db_path)
    else:
        raise ValueError("Ваш класс не определен")

def rockerboy_lifeway(db_path):
    db_path = db_path
    def rockerboy_init(db_path):
        rockerboy_type(db_path)
        group_or_solo = randint(1,2)
        if group_or_solo < 2:
            print("Ты выступаешь один")
            group_before = randint(1,2)
            if group_before < 2:
                print("Раньше ты выступал в группе")
                rockerboy_group_collapse(db_path)               
            else:
                print("Ты выступаешь почти всегда один")
                rockerboy_where_perform(db_path)
        else:
            print("Ты выступаешь в группе")
            rockerboy_where_perform(db_path)

        rockerboy_anthoganist(db_path)

    def rockerboy_type(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="ROCKERBOY_TYPE",
            record_id=gend10(),
            fields=["text"],
            message_format="Какой вы Рокеробой: {text}"
        )

    def rockerboy_group_collapse(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="ROCKERBOY_GROUP_COLLAPSE",
            record_id=gend6(),
            fields=["text"],
            message_format="Вы ушли из группы из-за: {text}"
        )

    def rockerboy_where_perform(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="ROCKERBOY_WHERE_PERFORM",
            record_id=gend6(),
            fields=["text"],
            message_format="Вы выступаете: {text}"
        )

    def rockerboy_anthoganist(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="ROCKERBOY_ANTHOGANIST",
            record_id=gend6(),
            fields=["text"],
            message_format="За вами охотится: {text}"
        )

    rockerboy_init(db_path)

def solo_lifeway(db_path):
    db_path = db_path
    def solo_init(db_path):
        solo_type(db_path)
        solo_morale(db_path)
        solo_work(db_path)
        solo_anthoganist(db_path)
    
    def solo_type(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="SOLO_TYPE",
            record_id=gend6(),
            fields=["text"],
            message_format="Какой вы Соло: {text}"
        )

    def solo_morale(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="SOLO_MORALE",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваш моральный кодекс: {text}"
        )

    def solo_work(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="SOLO_WORK",
            record_id=gend6(),
            fields=["text"],
            message_format="Вы обычно работаете в: {text}"
        )

    def solo_anthoganist(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="SOLO_ANTHOGANIST",
            record_id=gend6(),
            fields=["text"],
            message_format="За вами охотится: {text}"
        )
    
    solo_init(db_path)

def netrunner_lifeway(db_path):
    db_path = db_path
    def netrunner_init(db_path):
        netrunner_type(db_path)

        partner = randint(1,2)
        if partner < 2:
            print("Вы работаете в одиночку")
        else:
            print("Вы работаете не один")
            netrunner_partner(db_path)

        netrunner_workspace(db_path)
        netrunner_client(db_path)
        netrunner_program(db_path)
        netrunner_anthoganist(db_path)

    def netrunner_type(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="NETRUNNER_TYPE",
            record_id=gend6(),
            fields=["text"],
            message_format="Какой вы Нетраннер: {text}"
        )

    def netrunner_partner(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="NETRUNNER_PARTNER",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваш партнер: {text}"
        )

    def netrunner_workspace(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="NETRUNNER_WORKSPACE",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваше рабочее место: {text}"
        )

    def netrunner_client(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="NETRUNNER_CLIENT",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваши клиенты: {text}"
        )

    def netrunner_program(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="NETRUNNER_PROGRAM",
            record_id=gend6(),
            fields=["text"],
            message_format="Где вы берете свои программы: {text}"
        )

    def netrunner_anthoganist(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="NETRUNNER_ANTHOGANIST",
            record_id=gend6(),
            fields=["text"],
            message_format="За вами охотится: {text}"
        )
    
    netrunner_init(db_path)

def tech_lifeway(db_path):
    db_path = db_path
    def tech_init(db_path):
        tech_type(db_path)

        partner = randint(1,2)
        if partner < 2:
            print("Вы работаете в одиночку")
        else:
            print("Вы работете не один")
            tech_partner(db_path)

        tech_workspace(db_path)
        tech_client(db_path)
        tech_material(db_path)
        tech_anthoganist(db_path)

    def tech_type(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="TECH_TYPE",
            record_id=gend10(),
            fields=["text"],
            message_format="Какой вы Техник: {text}"
        )

    def tech_partner(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="TECH_PARTNER",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваш партнер: {text}"
        )

    def tech_workspace(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="TECH_WORKSPACE",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваше рабочее место: {text}"
        )

    def tech_client(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="TECH_CLIENT",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваши основные клиенты: {text}"
        )

    def tech_material(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="TECH_MATERIAL",
            record_id=gend6(),
            fields=["text"],
            message_format="Вы получаете материалы : {text}"
        )

    def tech_anthoganist(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="TECH_ANTHOGANIST",
            record_id=gend6(),
            fields=["text"],
            message_format="За вами охотится: {text}"
        )
    
    tech_init(db_path)

def medtech_lifeway(db_path):
    db_path = db_path
    def medtech_init(db_path):
        medtech_type(db_path)

        partner = randint(1,2)
        if partner < 2:
            print("Вы работаете в одиночку")
        else:
            print("Вы работаете не один")
            medtech_partner(db_path)
        
        medtech_workspace(db_path)
        medtech_client(db_path)
        medtech_material(db_path)
    
    def medtech_type(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="MEDTECH_TYPE",
            record_id=gend10(),
            fields=["text"],
            message_format="Какой вы Медтехник: {text}"
        )

    def medtech_partner(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="MEDTECH_PARTNER",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваш партнер: {text}"
        )

    def medtech_workspace(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="MEDTECH_WORKSPACE",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваше рабочее место: {text}"
        )

    def medtech_client(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="MEDTECH_CLIENT",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваши клиенты: {text}"
        )
    
    def medtech_material(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="MEDTECH_MATERIAL",
            record_id=gend6(),
            fields=["text"],
            message_format="Вы получаете материалы: {text}"
        )
    
    medtech_init(db_path)

def media_lifeway(db_path):
    db_path = db_path

    def media_init(db_path):
        media_type(db_path)
        media_publicity(db_path)
        media_ethic(db_path)
        media_story(db_path)
    
    def media_type(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="MEDIA_TYPE",
            record_id=gend6(),
            fields=["text"],
            message_format="Какой вы Медиа: {text}"
        )

    def media_publicity(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="MEDIA_PUBLICITY",
            record_id=gend6(),
            fields=["text"],
            message_format="Вы находите огласку: {text}"
        )

    def media_ethic(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="MEDIA_ETHICS",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваша этика: {text}"
        )
    
    def media_story(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="MEDIA_STORY",
            record_id=gend6(),
            fields=["text"],
            message_format="Вы рассказываете о: {text}"
        )
    
    media_init(db_path)

def lowyer_lifeway(db_path):
    db_path = db_path
    def lowyer_init(db_path):
        lowyer_type(db_path)
        lowyer_jurisdiction(db_path)
        lowyer_corrupt(db_path)
        lowyer_anthoganist(db_path)
        lowyer_target(db_path)
    
    def lowyer_type(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="LOWYER_TYPE",
            record_id=gend6(),
            fields=["text"],
            message_format="Какой вы Законник: {text}"
        )
    
    def lowyer_jurisdiction(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="LOWYER_JURISDICTION",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваша юрисдикция: {text}"
        )

    def lowyer_corrupt(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="LOWYER_CORRUPT",
            record_id=gend6(),
            fields=["text"],
            message_format="Насколько вы коррумпированы: {text}"
        )

    def lowyer_anthoganist(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="LOWYER_ANTHOGANIST",
            record_id=gend6(),
            fields=["text"],
            message_format="За вами охотится: {text}"
        )
    
    def lowyer_target(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="LOWYER_TARGET",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваша основная цель: {text}"
        )
    
    
    lowyer_init(db_path)

def corp_lifeway(db_path):
    db_path = db_path
    def corp_init(db_path):
        corp_type(db_path)
        corp_department(db_path)
        corp_goodbad(db_path)
        corp_where(db_path)
        corp_anthoganist(db_path)
        corp_boss(db_path)

    def corp_type(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="CORP_TYPE",
            record_id=gend10(),
            fields=["text"],
            message_format="Ваша компания занимается: {text}"
        )

    def corp_department(db_path):
            get_and_print_record(
            db_path=db_path,
            table_name="CORP_DEPARTMENT",
            record_id=gend6(),
            fields=["text"],
            message_format="Вы работаете в отделе: {text}"
        )

    def corp_goodbad(db_path):
            get_and_print_record(
            db_path=db_path,
            table_name="CORP_GOOD_BAD",
            record_id=gend6(),
            fields=["text"],
            message_format="Насколько хороша/плоха ваша корпа: {text}"
        )

    def corp_where(db_path):
            get_and_print_record(
            db_path=db_path,
            table_name="CORP_WHERE",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваша корпа находится: {text}"
        )

    def corp_anthoganist(db_path):
            get_and_print_record(
            db_path=db_path,
            table_name="CORP_ANTHOGANIST",
            record_id=gend6(),
            fields=["text"],
            message_format="За вами охотится: {text}"
        )

    def corp_boss(db_path):
            get_and_print_record(
            db_path=db_path,
            table_name="CORP_BOSS",
            record_id=gend6(),
            fields=["text"],
            message_format="Отношения с вашим босом: {text}"
        )

    corp_init(db_path)

def nomad_lifeway(db_path):
    db_path = db_path
    def nomad_init(db_path):
        nomad_swarm(db_path)
        nomad_based_on(db_path)
        nomad_type(db_path)
        nomad_philosophy(db_path)
        nomad_anthoganist(db_path)
    
    def nomad_based_on(db_path):
        match gend6() / 2:
            case 1:
                print("Ваша стая базируется на земле")
                nomad_land(db_path)
            case 2:
                print("Ваша стая базируется в воздухе")
                nomad_air(db_path)
            case 3:
                print("Ваша стая базируется в море")
                nomad_ocean(db_path)


    def nomad_swarm(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="NOMAD_SWARM",
            record_id=gend6(),
            fields=["text"],
            message_format="Размер вашей стаи: {text}"
        )
    
    def nomad_land(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="NOMAD_LAND",
            record_id=gend10(),
            fields=["text"],
            message_format="На суше ваша стая занимается: {text}"
        )
    
    def nomad_air(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="NOMAD_AIR",
            record_id=gend6(),
            fields=["text"],
            message_format="В воздухе ваша стая занимается: {text}"
        )

    def nomad_ocean(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="NOMAD_OCEAN",
            record_id=gend6(),
            fields=["text"],
            message_format="В море ваша стая занимается: {text}"
        )

    def nomad_type(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="NOMAD_TYPE",
            record_id=gend6(),
            fields=["text"],
            message_format="Для клана вы занимаетесь: {text}"
        )

    def nomad_philosophy(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="NOMAD_PHILOSOPHY",
            record_id=gend6(),
            fields=["text"],
            message_format="Философия вашей стаи: {text}"
        )
    def nomad_anthoganist(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="NOMAD_ANTHOGANIST",
            record_id=gend6(),
            fields=["text"],
            message_format="За вами охотится: {text}"
        )
    
    nomad_init(db_path)

def fixer_lifeway(db_path):
    db_path = db_path
    def fixer_init(db_path):
        fixer_type(db_path)
        partner = randint(1,2)
        if partner < 2:
            print("Вы работаете в одиночку")
        else:
            print("Вы работаете не один")
            fixer_partner(db_path)
        fixer_office(db_path)
        fixer_client(db_path)
        fixer_anthoganist(db_path)

    def fixer_type(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="FIXER_TYPE",
            record_id=gend10(),
            fields=["text"],
            message_format="Какой вы Фиксер: {text}"
        )

    def fixer_partner(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="FIXER_PARTNER",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваш партнер: {text}"
        )

    def fixer_office(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="FIXER_OFFICE",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваш офис: {text}"
        )

    def fixer_client(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="FIXER_CLIENT",
            record_id=gend6(),
            fields=["text"],
            message_format="Ваши клиенты: {text}"
        )

    def fixer_anthoganist(db_path):
        get_and_print_record(
            db_path=db_path,
            table_name="FIXER_ANTHOGANIST",
            record_id=gend6(),
            fields=["text"],
            message_format="За вами охотится: {text}"
        )

    fixer_init(db_path)
