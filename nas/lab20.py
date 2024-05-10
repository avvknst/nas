from PIL import Image, ImageDraw

# Создаем изображение
width, height = 1050, 200
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Рисуем слово "А Н А С"
draw.line((50, 150, 100, 50), fill='red', width=5)
draw.line((100, 50, 150, 150), fill='red', width=5)
draw.line((125, 100, 75, 100), fill='red', width=5)

draw.line((175, 50, 175, 150), fill='pink', width=5)
draw.line((175, 100, 225, 100), fill='pink', width=5)
draw.line((225, 50, 225, 150), fill='pink', width=5)

draw.line((250, 150, 300, 50), fill='red', width=5)
draw.line((300, 50, 350, 150), fill='red', width=5)
draw.line((325, 100, 275, 100), fill='red', width=5)

draw.arc((375, 50, 475, 150), start=40, end=300, fill='yellow', width=5)

# Рисуем слово "Т А С И Я"
draw.line((500, 50, 550, 50), fill='orange', width=5)
draw.line((525, 50, 525, 150), fill='orange', width=5)


draw.line((650, 150, 600, 50), fill='red', width=5)
draw.line((600, 50, 550, 150), fill='red', width=5)
draw.line((625, 100, 575, 100), fill='red', width=5)

draw.arc((675, 50, 775, 150), start=40, end=300, fill='yellow', width=5)

draw.line((875, 50, 875, 150), fill='pink', width=5)
draw.line((875, 50, 825, 150), fill='pink', width=5)
draw.line((825, 50, 825, 150), fill='pink', width=5)

draw.line((900, 150, 950, 95), fill='purple', width=5)
draw.line((950, 50, 950, 150), fill='purple', width=5)
draw.arc((900, 50, 1000, 100), start=90, end=-90, fill='purple', width=5)
# Сохраняем изображение
image.save("Anastasia.png")