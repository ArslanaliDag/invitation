import os
from PIL import Image, ImageDraw, ImageFont

# Путь к файлу с именами и изображением
names_file = 'invitation_names.txt'
image_file = 'invitation.jpg'
output_dir = 'invitations'

# Размер изображения в миллиметрах и разрешение
width_mm, height_mm = 209.97, 260.01
resolution = 300  # dpi

# Конвертация миллиметров в пиксели
mm_to_pixels = lambda mm: int(mm / 25.4 * resolution)
width_px = mm_to_pixels(width_mm)
height_px = mm_to_pixels(height_mm)

# Создаём папку для сохранения, если её нет
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Загружаем список имён из файла (имена в столбец)
with open(names_file, 'r', encoding='utf-8') as file:
    names = file.read().splitlines()

# Загружаем изображение
image = Image.open(image_file)
image = image.resize((width_px, height_px))  # Изменяем размер в пикселях

# Загружаем шрифт Book Antiqua
font_path = 'Book_Antiqua.ttf'  # Путь к шрифту
font_size = 80  # Размер шрифта
font = ImageFont.truetype(font_path, font_size)

# Параметры для размещения текста на изображении
text_y_position = 1810  # Вертикальная позиция текста
text_color = (255, 0, 0)  # Красный цвет текста (RGB)

# Функция для центрирования текста по горизонтали
def get_centered_position(text, font, image_width):
    # textbbox возвращает координаты рамки, обрамляющей текст (x0, y0, x1, y1)
    text_bbox = ImageDraw.Draw(image).textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]  # Ширина текста
    centered_x_position = (image_width - text_width) // 2
    return centered_x_position

# Проходим по списку имён и добавляем их на изображение
for name in names:
    # Копируем изображение для каждого имени
    img_copy = image.copy()
    draw = ImageDraw.Draw(img_copy)
    
    # Рассчитываем позицию для центрирования текста
    text_x_position = get_centered_position(name, font, width_px)
    
    # Размещаем имя на изображении
    draw.text((text_x_position, text_y_position), name, fill=text_color, font=font)
    
    # Преобразуем имя для файла: убираем пробелы и заменяем на _
    file_name = name.replace(' ', '_').replace('ь', '').replace('ё', 'е')
    
    # Сохраняем изображение с именем
    img_copy.save(os.path.join(output_dir, f'{file_name}.jpeg'))

print("Готово! Все изображения сохранены в папке invitations.")