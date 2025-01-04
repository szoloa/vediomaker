from moviepy import *

bg = ColorClip(size=(1920, 1080), color=(255,255,255))

clip = VideoFileClip("input.mp4")

clip = clip.resized((1920*0.8, 1080*0.8))

txt_clip = TextClip(text="My Holidays 2013",font='Hack-Regular',font_size=160, color='black')

txt_clip = txt_clip.with_end(clip.end)

bg = bg.with_end(clip.end)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([bg, clip, txt_clip])

video.fps=25

# video.preview()

video.write_videofile("output.mp4")
