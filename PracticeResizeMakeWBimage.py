import datetime
import multiprocessing as mp
from PIL import Image
from queue import Empty


def resize_image(image_paths, pipe: mp.Pipe, stop_event: mp.Event):  # queue):
    for image_path in image_paths:
        image_rs = Image.open(image_path)
        image_rs = image_rs.resize((800, 600))
        image_rs.save(image_path)
        # queue.put((image_path, image_rs))
        pipe.send(image_path)
    stop_event.set()


def change_color(pipe: mp.Pipe, stop_event: mp.Event):  # queue):
    # while True:
    while not stop_event.is_set():
        # try:
        # image_path, image_bw = queue.get(timeout=5)
        image_path = pipe.recv()
        # except Empty as e:
        #     break
        image_bw = Image.open(image_path)
        image_bw = image_bw.convert('L')
        image_bw.save(image_path)


if __name__ == '__main__':
    data = []
    # queue = mp.Queue()
    conn1, conn2 = mp.Pipe()
    stop_event = mp.Event()
    for image in range(1, 11):
        if (image < 3) or (image > 7):
            data.append(f'./images/img_{image}.jpg')
        else:
            data.append(f'./images/img_{image}.png')

    resize_proccess = mp.Process(target=resize_image, args=(data, conn1, stop_event))
    change_proccess = mp.Process(target=change_color, args=(conn2, stop_event))

    start_time = datetime.datetime.now()

    resize_proccess.start()
    change_proccess.start()

    resize_proccess.join()
    change_proccess.join()

    end_time = datetime.datetime.now()
    print(f'Time: {end_time - start_time}')
    # Queue
    # Time: 0:00:05.336954
    # Pipe
    # Time: 0:00:08.340927
