# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 21:28:12 2024

@author: Revlis_user
"""

#%%
"Import libraries"

from params import *


df = pd.read_csv("task100k.csv")
# client_credentials_manager = SCC(client_id, client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

song_idx = df.id

# try:
#     audio_features = sp.audio_features(song_idx[5])[0]
#     track = sp.track(song_idx[5])
#     print(track)
# except spotipy.exceptions.SpotifyException as e:
#     print(f"Spotify API 請求失敗: {e}")

# feature_name = list(audio_features.keys())
# feature_name = ['id'] + [n for n in feature_name if n != 'id']
# df_full_feature = pd.DataFrame(columns=feature_name)
# df_full_feature.loc[len(df_full_feature)] = audio_features
# df_full_feature.to_csv('df_full_feature.csv')

df_full_feature = pd.read_csv('df_full_feature.csv')
# df_full_feature = df_full_feature.drop(df_full_feature.columns[0], axis=1)

# df_full_feature = pd.DataFrame(columns = df_full_feature.columns)
# df_full_feature.to_csv('df_full_feature.csv', index = False)
