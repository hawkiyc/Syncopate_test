# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:19:40 2024

@author: Revlis_user
"""

#%%
"Import Libraries"

import os
from dotenv import load_dotenv
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials as SCC
from spotipy.oauth2 import SpotifyOAuth
import requests
import time

#%%
"Set Parameters"

load_dotenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
