import pandas as pd
import json
import requests
import time

token = "df15323ca5b4485d14d2eac235a281f221d1dde2" 

start_games = 5455430
end_games = 5455684

from time import sleep
import random
from pandas import json_normalize

# Lista para almacenar los datos de todos los partidos
event_data = []

while start_games <= end_games:
    url = f'https://searchapi.wyscout.com/api/v2/matches/{start_games}/events.json?lang=es&skip_players=false&token={token}&groupId=1059060&subgroupId=93476'
    headers = {
        'Origin': 'https://platform.wyscout.com',
        'Accept-Language': 'es-ES,es;q=0.9',
        'Referer': 'https://platform.wyscout.com/app/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    print(f"Status code for match {start_games}: {r.status_code}")

    
    if r.status_code == 200:
        
        data = r.json()
        
        event_data.extend(data['events'])

    
    sleep(random.randint(1, 2))

 
    start_games += 1


df = pd.json_normalize(event_data)



#Exportar datos
df.to_csv('ligaMX23-24.csv', index=False)

df.shape

df.head(20)
