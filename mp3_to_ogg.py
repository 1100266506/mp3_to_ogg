import os
from pydub import AudioSegment
import shutil

# mp3 to wav converter
# Must import pydub using "python3 -m pip install pydub"
# Takes in a path that contains mp3 files and converts them into wavs
# It then takes the converted file and moves it to a target folder
# - make sure to edit the original path and target folder
# @author Benjamin Ahn
# @version 1.0

#insert path to folder containing mp3 files
original_path = "/home/benjamin/Music/playlist/"

#insert path to mp3 files
path, dir, mp3files = next(os.walk(original_path))

#creates target folder
target_folder = "/home/benjamin/Music/target"
if os.path.isdir(target_folder) == False:
    os.mkdir(target_folder)


for file in mp3files:
    #builds path to mp3 file
    length_name = len(file)
    source = original_path + "/" + file
    length = len(source)

    #changes path name from mp3 to wav
    target = source[:length - 4]
    target = target + ".ogg"
    length_target = len(target)


    #converts mp3 to wav
    sound = AudioSegment.from_mp3(source)
    sound.export(target, format = "ogg")
    shutil.move(target, target_folder + "/" + target[length_target - length_name:])
