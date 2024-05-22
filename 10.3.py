# Открываем файл с англо-русским словарем для чтения
with open('en-ru.txt', 'r', encoding='utf-8') as file:
    en_ru_dict = file.readlines()

# Создаем пустой словарь для русско-английского словаря
ru_en_dict = {}

# Заполняем русско-английский словарь
for line in en_ru_dict:
    english, russian = line.strip().split(' - ')
    russian_words = russian.split(', ')
    for word in russian_words:
        if word in ru_en_dict:
            ru_en_dict[word].append(english)
        else:
            ru_en_dict[word] = [english]

# Сортируем словарь по ключам (русским словам)
sorted_ru_en_dict = dict(sorted(ru_en_dict.items()))

# Открываем файл для записи русско-английского словаря
with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for russian, english_list in sorted_ru_en_dict.items():
        # Объединяем английские слова через запятую
        english = ', '.join(english_list)
        # Записываем строку в файл
        file.write(f"{russian} – {english}n")

print("Русско-английский словарь создан и сохранен в файле ru-en.txt.")
