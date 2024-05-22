from PIL import Image, ImageEnhance, ImageFilter
import os

source_folder = r'C:\1-md-20-Fedorov\processed_images'
destination_folder = r'C:\1-md-20-Fedorov\n_images'

# Список имен файлов изображений для обработки
image_files = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

# Применение фильтра к каждому изображению
for image_file in image_files:
    try:
        # Полный путь к исходному изображению
        source_image_path = os.path.join(source_folder, image_file)

        # Загрузка изображения
        with Image.open(source_image_path) as img:
            # Применение фильтра SMOOTH
            emboss_img = img.filter(ImageFilter.EMBOSS)

            # Полный путь к обработанному изображению
            destination_image_path = os.path.join(destination_folder, f"emboss_{image_file}")

            # Сохранение обработанного изображения
            emboss_img.save(destination_image_path)

    except IOError:
        print(
            f"Ошибка при открытии изображения {image_file}. Убедитесь, что файл существует и имеет правильный формат.")