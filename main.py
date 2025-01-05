from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx import FadeIn, FadeOut
from moviepy.video.tools import subtitles
 
# 加载视频剪辑
clip = VideoFileClip("input.mp4")
 
# 添加淡入和淡出效果
clip = FadeIn(clip, 2)  # 从开始处淡入2秒
clip = FadeOut.FadeOut(clip, 2)  # 从结束处淡出2秒
 
# 添加字幕
subtitles_txt = [
    ("Hello, World!", 1),  # 在1秒时显示 "Hello, World!"
    ("Welcome to MoviePy", 3),  # 在3秒时显示 "Welcome to MoviePy"
]
# clip = subtitles(clip, subtitles_txt)
 
# 保存视频
clip.write_videofile("output.mp4")
