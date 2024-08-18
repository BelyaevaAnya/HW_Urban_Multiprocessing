import random
import time
from threading import Thread
from queue import Queue


class Bun(Thread):
    def __init__(self, queue: Queue):
        self.queue = queue
        super().__init__()

    def run(self):
        while True:
            time.sleep(3)
            if random.random() > 0.5:
                self.queue.put('burnt bun')
            else:
                self.queue.put('normal bun')


class Patty(Thread):

    def __init__(self, queue, count):
        self.queue = queue
        self.count = count
        super().__init__()

    def run(self):
        while self.count:
            print(f'Queue size: {self.queue.qsize()}')
            bun = self.queue.get(timeout=5)
            if bun == 'normal bun':
                time.sleep(0.1)
                self.count -= 1
            print(f'We have {self.count} buns')


queue = Queue(maxsize=40)

t1 = Bun(queue)
t2 = Patty(queue, 20)

t1.start()
t2.start()

t1.join()
t2.join()
