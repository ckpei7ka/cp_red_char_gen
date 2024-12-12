SELECT 
    CULT_BACK.name AS region_name,   -- Имя региона
    LANG.name AS language_name      -- Имя языка
FROM 
    REGION_LANGUAGES
JOIN 
    CULT_BACK ON REGION_LANGUAGES.region_id = CULT_BACK.id   -- Соединение с таблицей регионов
JOIN 
    LANG ON REGION_LANGUAGES.language_id = LANG.id 	-- Соединение с таблицей языков
ORDER BY 
    CULT_BACK.name, LANG.name;  -- Сортировка по имени региона и имени языка
