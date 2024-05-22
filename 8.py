from PIL import Image

# Загрузка и обрезка изображения
def crop_image(input_path, output_path, crop_box):
    image = Image.open(input_path)
    cropped_image = image.crop(crop_box)
    cropped_image.save(output_path)
    return output_path

# Показ открытки на экране
def show_card(image_path):
    image = Image.open(image_path)
    image.show()

# Обрезка изображения
input_image_path = 'C:\1-md-20-Fedorov\osiris-logo.jpg'  # Укажите путь к вашему изображению
output_image_path = 'cropped_image.jpg'  # Укажите новое имя файла
crop_box = (100, 100, 400, 400)  # Укажите координаты в соответствии с вашими требованиями
cropped_image_path = crop_image(input_image_path, output_image_path, crop_box)


