import json
import re
import pandas as pd

def json_to_df(file):
  f = open(file)
  data = json.load(f)
  artist = data['name']
  all_lyrics = []
  song_name = []
  for song in data['songs']:
    lyrics = song['lyrics']
    parsed_lyrics = re.sub(":\s.*?\]","]",lyrics,flags=re.DOTALL)
    parsed_lyrics_2 = re.sub("\[Produced.*?\[","[",parsed_lyrics,1,flags=re.DOTALL)
    all_lyrics.append(parsed_lyrics_2)
    song_name.append(song['title'])
  print(all_lyrics[16])
  print(song_name[16])
  df = pd.DataFrame({'song title':song_name,'lyrics':all_lyrics})
  df['artist'] = artist
  return df
