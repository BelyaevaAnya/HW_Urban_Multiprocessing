import pprint

import requests
from threading import Thread

# www.example.com/search?q=some_query&type=music&genre=classic

ACCESS_TOKEN = 'Zx9ft7WLT3X6zKOTZWoI3_Tn_hy-O8lJk_v1O1JBuYYOwIkvGKsMG-D43vcfX5al'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'

genre = requests.get(RANDOM_GENRE_API_URL).json()

data = requests.get(GENIUS_API_URL, params={'access': ACCESS_TOKEN, 'q': genre})
pprint.pprint(data.json())
data = data.json()
song_id = data['response']['hits'][0]['result']['api_path']
print(f'{GENIUS_URL}{song_id}/apple_music_player')