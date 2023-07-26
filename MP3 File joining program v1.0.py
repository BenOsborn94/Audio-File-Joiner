#MP3 File joining program v1.0-2023-07-11

#import modules

import os
import time
import pydub
from pydub import AudioSegment
import re

#Introduce Program

print()
print('This program concatenates multiple MP3 files into one long MP3 file.')
print('______________________________________________')
print()
print('Enter the file path for the folder containing documents requiring analysis:')

# input and process the containing folder filepath

path = input()
path = path.replace(os.sep, '/')

pathend = path.endswith('/')
if pathend == False:
    path = path + '/'
else:
    path = path

os.chdir(path)

# list the files in the directory

audio_list = os.listdir()

print('______________________________________________')
print()
print('List of Files in the Directory:')
print(audio_list)
print('______________________________________________')
print()

# input desired output file name

print('Enter the desired name for the output file:')

filename = input()

# advise user of the virtue of patience

print('______________________________________________')
print()
print('Program is reviewing files in the directory and processing into a joined file. This may take a few minutes.')
print('______________________________________________')
print()

# process the files in the directory

playlist_songs = [AudioSegment.from_mp3(mp3_file) for mp3_file in audio_list] 

combined = AudioSegment.empty()
combined = playlist_songs[0]

for song in playlist_songs[1:]:
   combined = combined.append(song)

#define output file

combined.export(path+"/"+filename+".mp3" , format="mp3")

print('Audio File Complete and exported to Source File path')
input("Press Enter key to exit")
