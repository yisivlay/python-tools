import speech_recognition as sr
import moviepy.editor as mp

# Source file path
clip = mp.VideoFileClip(r"video.mp4")
# Target file path
clip.audio.write_audiofile(r"video.wav")
r = sr.Recognizer()
audio = sr.AudioFile("video.wav")
with audio as source:
    audio_file = r.record(source)
    result = r.recognize_google(audio_file)
# Target file text
with open('script.txt', mode='w') as file:
    file.write("Recognized Speech:\n")
    file.write(result)
print("ready!")
