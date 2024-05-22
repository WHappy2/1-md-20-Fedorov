from PIL import Image

image = Image.open(r'C:\1-md-20-Fedorov\osiris-logo.jpg')
image.show()

width, height = image.size
format = image.format
mode = image.mode

print(f"Размер изображения: {width}x{height} пикселей")
print(f"Формат изображения: {format}")
print(f"Цветовая модель: {mode}")