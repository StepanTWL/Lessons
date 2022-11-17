import time
from PIL import Image


def create_image(image_path):
    image_pixels_list = []
    img = Image.open(image_path)
    pixels = img.load()

    # Добавляем вертикальные линии в обратном порядке
    for w in range(1920):
        vertical_line = []
        for h in range(1080):
            vertical_line.append(pixels[w, h])
        image_pixels_list.insert(0, vertical_line)

    # Записываем готовые пиксели
    for w in range(1920):
        for h in range(1080):
            pixels[w, h] = image_pixels_list[w][h]
    img.save(f'result/{int(time.time())}.jpeg')

create_image('1.jpeg')