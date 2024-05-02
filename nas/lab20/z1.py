from PIL import Image, ImageDraw

# Создаем новое изображение
image = Image.new('RGB', (400, 200), 'white')
draw = ImageDraw.Draw(image)

# Нарисовать букву 'Н'
draw.line([(50, 50), (50, 150)], fill='black', width=5)
draw.line([(50, 50), (100, 50)], fill='black', width=5)
draw.line([(100, 50), (100, 150)], fill='black', width=5)

# Нарисовать букву 'а'
draw.arc((120, 50, 170, 100), start=180, end=0, fill='black', width=5)
draw.line([(145, 100), (145, 150)], fill='black', width=5)
draw.line([(145, 100), (170, 100)], fill='black', width=5)

# Нарисовать букву 'с'
draw.arc((190, 50, 240, 100), start=0, end=270, fill='black', width=5)
draw.arc((190, 100, 240, 150), start=90, end=360, fill='black', width=5)

# Нарисовать букву 'т'
draw.line([(260, 50), (310, 50)], fill='black', width=5)
draw.line([(285, 50), (285, 150)], fill='black', width=5)

# Нарисовать букву 'я'
draw.arc((330, 50, 380, 100), start=0, end=180, fill='black', width=5)
draw.line([(355, 100), (355, 150)], fill='black', width=5)
draw.line([(355, 100), (380, 100)], fill='black', width=5)

# Сохранить изображение
image.save('name.jpg')
