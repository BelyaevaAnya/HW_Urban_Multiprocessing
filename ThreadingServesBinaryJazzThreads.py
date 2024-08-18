import pprint
import queue
import requests
from threading import Thread

# www.example.com/search?q=some_query&type=music&genre=classic

ACCESS_TOKEN = 'Zx9ft7WLT3X6zKOTZWoI3_Tn_hy-O8lJk_v1O1JBuYYOwIkvGKsMG-D43vcfX5al'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'
all_songs = []
class GetGenre(Thread):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        genre = requests.get(RANDOM_GENRE_API_URL).json()
        self.queue.put(genre)
class Genius(Thread):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        genre = self.queue.get()
        data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})
        data = data.json()
        try:
            song_id = data['response']['hits'][0]['result']['api_path']
            all_songs.append(f'{GENIUS_URL}{song_id}/apple_music_player')
        except IndexError as e:
            pass


queue = queue.Queue()
genre_list = []
genius_list = []
for _ in range(10):
    t = GetGenre(queue)
    t.start()
    genre_list.append(t)

for _ in range(10):
    t = Genius(queue)
    t.start()
    genius_list.append(t)

for t in genius_list:
    t.join()

print(all_songs)
print(len(all_songs))