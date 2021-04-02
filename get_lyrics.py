import lyricsgenius as lg
import pandas as pd
import json as j
import requests
from bs4 import BeautifulSoup
import os
import re

genius = lg.Genius('Fd4M0Y2_mUpjXFjmSzQrjtOnR_kTjhgc6KyubGPeSz-C0v4Or8tgnorMEzV_gkbv',
                   skip_non_songs=True,
                   excluded_terms=["(Remix)", "(Live)"])

artist_names = ['Eminem', 'Kendrick Lamar', 'Etta James', 'MF Doom', 'The Beatles', 'Smokey Robinson', 'ABBA', 'Al Green', 'Prince', 'Anderson .Paak', 'James Brown']

artists = {}
fails = []
for artist in artist_names:
    tries = 0
    while tries < 100:
        try:
            tries += 1
            artists[artist] = genius.search_artist(artist, max_songs = 50, include_features=False)
            artists[artist].save_lyrics()
            break
        except:
            pass

    
