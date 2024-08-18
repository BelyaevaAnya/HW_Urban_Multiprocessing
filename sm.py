import pprint

all_images = []
for image in range(1, 11):
    if (image < 4) or (image > 7):
        all_images.append(f'./images/img_{image}.jpg')
    else:
        all_images.append(f'./images/img_{image}.png')
pprint.pprint(all_images)