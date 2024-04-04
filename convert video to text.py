pip install opencv-python moviepy SpeechRecognition
import cv2
from moviepy.editor import VideoFileClip
import speech_recognition as sr
def extract_audio(video_path, audio_path):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)
video_path = 'path/to/video.mp4'
audio_path = 'path/to/audio.wav'
extract_audio(video_path, audio_path)
def audio_to_text(audio_path):
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
    return text
audio_path = 'path/to/audio.wav'
text = audio_to_text(audio_path)
print(text)