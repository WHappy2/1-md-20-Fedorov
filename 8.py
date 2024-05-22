from PIL import Image, ImageDraw, ImageFont

# Путь к исходному изображению
image_path = r'C:\1-md-20-Fedorov\osiris-logo.jpg'  # Замените на путь к вашему изображению

# Загрузка изображения
image = Image.open(image_path)

# Определение области для обрезки (left, upper, right, lower)
crop_box = (100, 100, 400, 400)  # Задайте координаты в соответствии с вашими требованиями
cropped_image = image.crop(crop_box)

# Спросите у пользователя имя
name_to_congratulate = input("Введите имя того, кого вы хотите поздравить: ")

# Добавление текста на открытку
draw = ImageDraw.Draw(cropped_image)
# Убедитесь, что файл шрифта arial.ttf находится в доступном месте или используйте другой шрифт
font_path = "arial.ttf"  # Или путь к другому файлу шрифта, если он не в стандартном месте
font = ImageFont.truetype(font_path, 20)

# Вычисление позиции текста
# Используем метод getsize объекта font для получения размера текста
text_width, text_height = font.getsize(text)
text_x = (cropped_image.width - text_width) / 2
text_y = 20  # Отступ сверху

# Рисование текста
draw.text((text_x, text_y), text, font=font, fill="black")  # Выберите цвет текста

# Сохранение новой открытки
new_card_path = 'congratulation_card.png'  # Сохранение в формате PNG
cropped_image.save(new_card_path)

# Показать открытку
cropped_image.show()
