# Потоки работают в рамках процесса
# Процесс просто работает
# Потоки могут работать только конкурентно
# Tradebased-параллелизм основанный на тредах(потоках)
# Processbased-параллелизм основанный на процессах
# import multiprocessing
import datetime
# no multi processing
from PIL import Image
import datetime


def resize_image(image_path):
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    image.save(image_path)


start = datetime.datetime.now()
for i in range(1, 11):
    image_path = f'./images/img_{i}.jpg'
    try:
        resize_image(image_path)
    except FileNotFoundError:
        image_path = f'./images/img_{i}.png'
        resize_image(image_path)
end = datetime.datetime.now()
print(f'Time: {end - start}')
# Time: 0:00:02.040452