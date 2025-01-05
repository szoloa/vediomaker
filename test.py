from moviepy import *

bg = ColorClip(size=(1920, 1080), color=(255,255,255))

clip = VideoFileClip("input.mp4")

clip = clip.resized(0.45)

clip = clip.with_position((640, 60))

txt_clip = TextClip(text="The girl \nI want",font='simsun',font_size=84, color='black')
txt_clip = txt_clip.with_position((120, 1080/4-84/2))

txt_clip_2 = TextClip(text="What I \nlooks like",font='simsun',font_size=84, color='black')
txt_clip_2 = txt_clip_2.with_position((120, 1080*3/4-84/2))

txt_clip = txt_clip.with_end(clip.end)
txt_clip_2 = txt_clip_2.with_end(clip.end)

bg = bg.with_end(clip.end)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([bg, clip, txt_clip, txt_clip_2])

video.preview(audio=False)

# video.write_videofile("output.mp4")
