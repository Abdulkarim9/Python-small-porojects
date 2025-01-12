import os
from moviepy.editor import *


mp4_path = input("Enter mp4 full path: ")

mp3_path = input("Enter output path with the file name and change '.mp4' to '.mp3': ")

video = VideoFileClip(mp4_path)
video.audio.write_audiofile(mp3_path)