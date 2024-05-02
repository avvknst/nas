from PIL import Image

image = Image.open('risunok5.jpeg')
width, height = image.size
pixels = image.load()
new_image = Image.new('RGB', (width, height))

# Проходимся по каждому пикселю и преобразуем его
for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        # Находим максимальное и минимальное значение среди компонент пикселя
        max_value = max(r, g, b)
        min_value = min(r, g, b)
        # Записываем минимальное значение в красную компоненту, а максимальное в синюю
        new_color = (min_value, g, max_value)
        # Записываем преобразованный пиксель в новое изображение (переворачиваем по вертикали)
        new_image.putpixel((x, height - y - 1), new_color)

new_image.save('risunok6.jpg')
image.close()
new_image.close()