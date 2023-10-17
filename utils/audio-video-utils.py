from moviepy.editor import VideoFileClip, AudioFileClip

class AudioVideoUtils:
    
    # param audio - audio file name
    # param video - video file name
    def __init__(self, audio, video):
        self.audio = AudioFileClip(audio)
        self.video = VideoFileClip(video)
    
    # Method to add an audio file over a video
    def add_audio_to_video(self):
        return self.video.set_audio(self.audio)
    
    