# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:17:48 2024

@author: Revlis_user
"""

#%%
"Import libraries"

from params import *


df = pd.read_csv("task100k.csv")
client_credentials_manager = SCC(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

os.mkdir('mp3') if os.path.exists('mp3') is False else None

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'}
proxies = {
    "http": "http://51.89.134.68:80",
    "https": "https://43.134.68.153:3128"}

song_idx = df.id
no_sound_track = []

# try:
#     track = sp.track(song_idx[5])
#     print(track)
# except spotipy.exceptions.SpotifyException as e:
#     print(f"Spotify API 請求失敗: {e}")


for idx in song_idx:
    
    track = sp.track(idx)
    print(f'loading: {idx}')
    
    try:
        preview_url = track['preview_url']
        response = requests.get(preview_url, headers=headers, proxies=proxies)
        with open(f'mp3/{idx}.mp3', 'wb') as file:
            file.write(response.content)
    except:
        no_sound_track.append(idx)
    print(f"song id {idx} processed!!!")
    time.sleep(10)

if len(no_sound_track) != 0:
    df_filtered = df[~df.id.isin(no_sound_track)]
    df_filtered.to_csv("filtered.csv")
