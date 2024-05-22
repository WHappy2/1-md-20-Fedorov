from PIL import Image
# Замените 'original.jpg' на путь к вашему изображению
original_image_path = r'C:\1-md-20-Fedorov\osiris-logo.jpg'

# Открытие оригинального изображения
original_image = Image.open(original_image_path)

# Создание уменьшенной копии изображения
width, height = original_image.size
small_image = original_image.resize((width // 3, height // 3))
small_image.save(r'C:\1-md-20-Fedorov\small_image.jpg')  # Сохранение уменьшенного изображения

# Создание горизонтального зеркального образа изображения
horizontal_flip = original_image.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_flip.save(r'C:\1-md-20-Fedorov\horizontal_flip.jpg')  # Сохранение горизонтального зеркального образа

# Создание вертикального зеркального образа изображения
vertical_flip = original_image.transpose(Image.FLIP_TOP_BOTTOM)
vertical_flip.save(r'C:\1-md-20-Fedorov\vertical_flip.jpg')  # Сохранение вертикального зеркального образа

# Закрытие изображений
original_image.close()
small_image.close()
horizontal_flip.close()
vertical_flip.close()