import multiprocessing
from PIL import Image
import datetime


def resize_image(image_path):
    image_rs = Image.open(image_path)
    image_rs = image_rs.resize((800, 600))
    image_rs.save(image_path)


if __name__ == '__main__':
    with multiprocessing.Pool(processes=8) as pool:
        all_images = []
        for image in range(1, 11):
            if (image < 3) or (image > 7):
                all_images.append(f'./images/img_{image}.jpg')
            else:
                all_images.append(f'./images/img_{image}.png')
        start = datetime.datetime.now()
        pool.map(resize_image, all_images)
    end = datetime.datetime.now()
    print(f'Time: {end - start}')
    
# processes=4
# Time: 0:00:00.368820
# processes=8
# Time: 0:00:00.252149
