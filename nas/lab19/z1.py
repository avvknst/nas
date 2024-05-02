from PIL import Image

image = Image.open('risunok1.jpeg')
width, height = image.size
pixels = image.load()

# Инициализируем переменные для хранения суммы значений R, G, B
total_r = 0
total_g = 0
total_b = 0

# Проходимся по каждому пикселю и суммируем значения R, G, B
for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        total_r += r
        total_g += g
        total_b += b

# Вычисляем средние значения R, G, B
avg_r = total_r // (width * height)
avg_g = total_g // (width * height)
avg_b = total_b // (width * height)

print(f"Среднее значение R: {avg_r}, G: {avg_g}, B: {avg_b}")

# Создаем новое изображение, где каждый пиксель имеет среднее значение R, G, B
new_image = Image.new('RGB', (width, height), (avg_r, avg_g, avg_b))

new_image.save('risunok2.jpg')

image.close()