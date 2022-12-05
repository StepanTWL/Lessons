import time
from PIL import Image


def create_image(image_path):
    image_pixels_list = []
    img = Image.open(image_path)
    pixels = img.load()

    # Добавляем вертикальные линии в обратном порядке
    for w in range(669):
        vertical_line = []
        for h in range(667):
            vertical_line.append(pixels[w, h])
        image_pixels_list.insert(0, vertical_line)

    # Записываем готовые пиксели
    for w in range(669):
        for h in range(667):
            pixels[w, h] = image_pixels_list[w][h]
    img.save(f"{int(time.time())}.jpeg")


create_image('Example 01.jpg')
