import speech_recognition as sr
import subprocess


def convert_video_to_text(video_file_path):
    command = f"ffmpeg -i {video_file_path} -ab 160k -ar 44100 -vn -y audio.wav"
    subprocess.call(command, shell=True)
    recognizer = sr.Recognizer()

    with sr.AudioFile("audio.wav") as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="ru-RU")
            return text
        except sr.UnknownValueError:
            return "Голос не распознан"
        except sr.RequestError as e:
            return f"Ошибка при запросе к Google Web Speech API: {e}"
