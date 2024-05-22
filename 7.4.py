from PIL import Image, ImageDraw, ImageFont
import os
def add_watermark(input_image_path, output_image_path, watermark_text):
    image = Image.open(input_image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Используем метод textsize() объекта ImageDraw для получения размера текста
    text_width, text_height = draw.textsize(watermark_text, font)

    width, height = image.size
    margin = 10
    x = width - text_width - margin
    y = height - text_height - margin

    draw.text((x, y), watermark_text, font=font)
    image.save(output_image_path)

input_folder = "input_images"
output_folder = "output_images"
watermark_text = "Ваш водяной знак"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    input_image_path = os.path.join(input_folder, filename)
    output_image_path = os.path.join(output_folder, filename)
    add_watermark(input_image_path, output_image_path, watermark_text)

print("Водяные знаки добавлены к изображениям.")
