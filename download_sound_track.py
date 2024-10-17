# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:17:48 2024

@author: Revlis_user
"""

#%%
"Import libraries"

from params import *

#%%
"Load Full Feature and Soundtrack"

df = pd.read_csv("task100k.csv")
df_full_feature = pd.read_csv('df_full_feature.csv')
soundtrack_f_list = sorted(
    [f for f in os.listdir('./mp3') if f.endswith('.mp3')])

song_idx = sorted(list(df[~df.id.isin(df_full_feature.id)].id))

df_token = pd.read_excel("API_Token.xlsx")

"Rember to change api token, delete cache and set VPN before each execution"
"Rember to change api token, delete cache and set VPN before each execution"
"Rember to change api token, delete cache and set VPN before each execution"
client_id = df_token["client id"][0]
client_secret = df_token['client secret'][0]
client_credentials_manager = SCC(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
"Rember to change api token, delete cache and set VPN before each execution"
"Rember to change api token, delete cache and set VPN before each execution"
"Rember to change api token, delete cache and set VPN before each execution"

os.mkdir('mp3') if os.path.exists('mp3') is False else None
if os.path.exists('.cache'):
    os.remove('.cache')

for idx in song_idx:
    
    if idx not in soundtrack_f_list:
        track = sp.track(idx)
        try:
            preview_url = track['preview_url']
            response = requests.get(preview_url,)
            with open(f'mp3/{idx}.mp3', 'wb') as file:
                file.write(response.content)
        except:
            pass # Nothing to do
    else:
        pass # Nothing to do
    
    if idx not in soundtrack_f_list:
        audio_features = sp.audio_features(idx)[0]
        df_full_feature.loc[len(df_full_feature)] = audio_features
        df_full_feature.to_csv('df_full_feature.csv', index = False)
    else:
        pass #nothing to do
    
    print(f"song id {idx} processed!!!")

