import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while file.readline().strip():
            all_data.append(file.readline().rstrip())


if __name__ == '__main__':
    print(f'Вызов линейный')
    files_names = []
    for fl_num in range(1, 5):
        files_names.append(f'./Files/file {fl_num}.txt')
    start = datetime.datetime.now()
    for file in files_names:
        read_info(file)
    end = datetime.datetime.now()
    print(f'Время: {end - start}')
    print(f'Вызов многопроцессный')
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, files_names)
    end = datetime.datetime.now()
    print(f'Время: {end - start}')

# =>
# Вызов линейный
# Время: 0:00:03.081629
# Вызов многопроцессный
# Время: 0:00:01.303190
