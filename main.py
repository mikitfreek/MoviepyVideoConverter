
from moviepy.editor import *

import os.path
import glob
pth = 'in/'

files = list(map(os.path.basename, glob.iglob(pth+'*.mkv')))
print(files)

for file in files:

    clip = VideoFileClip('in/' + file)

    # clip = clip.subclip(0 * 60, (60 + 35) * 60)

    clip.write_videofile('out/' + os.path.splitext(file)[0] + '.mp4')


# clip.ipython_display(width=360)

# skip decoding encoding
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# ffmpeg_extract_subclip(name + ".mkv", start_time, end_time, targetname=name + ".mp4")
