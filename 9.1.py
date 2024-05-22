import os
from PIL import Image

# Создание каталога для обработанных изображений, если его нет
output_dir = "processed_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Обход файлов в заданной папке
input_dir = "input_images"
for filename in os.listdir(input_dir):
    filepath = os.path.join(input_dir, filename)
    if os.path.isfile(filepath):
        # Обработка только изображений с расширениями jpg и png
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Обработка изображения
            with Image.open(filepath) as img:
                # Пример обработки: изменение размера
                img = img.resize((300, 300))
                # Сохранение обработанного изображения в новом каталоге
                output_path = os.path.join(output_dir, filename)
                img.save(output_path)
                print(f"Изображение {filename} обработано и сохранено в {output_path}")
        else:
            print(f"Файл {filename} пропущен, так как не является изображением с расширением jpg или png")