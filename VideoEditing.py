import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "ffmpeg"
from moviepy.editor import VideoFileClip, concatenate_videoclips

video = VideoFileClip("VideoAssets/AvatarTestVideo.mp4")
clip1 = video.subclip(10, 20)
clip2 = video.subclip(40, 50)
clip3 = video.subclip(120, 140)
 
final = concatenate_videoclips([clip1,clip2,clip3])
final.write_videofile("movie.mp4", audio_codec = 'aac')

print("Hello World!")