from moviepy.editor import VideoFileClip, AudioFileClip

class AudioVideoUtils:
    
    # param audio - audio file name
    # param video - video file name
    def __init__(self, audio, video):
        self.translated_audio = AudioFileClip(audio)
        self.video = VideoFileClip(video)
        self.original_audio = video.audio                      
    
    # Method to add an audio file over a video
    def add_audio_to_video(self):
        self.trim_audio
        return self.video.set_audio(self.translated_audio)
    
    # Trims the audio file to match the duration of the video 
    def trim_audio(self):
        duration_difference = self.translated_audio.duration - self.video.duration
        if duration_difference <= 0:
            return
        else:
            self.audio = self.audio.subclip(0, self.video.duration)