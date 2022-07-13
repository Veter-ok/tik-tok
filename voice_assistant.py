# git push -f origin main
# brew remove portaudio
# brew install portaudio
# pip3 install pyAudio
# pip3 install gTTS
# pip3 install SpeechRecognition
import speech_recognition as sr
import os

def talk(text, voice="Milena"):
	print(text)
	os.system(f"say -v {voice} {text}")


def listening():
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
		print("Слушаю...")
		recognizer.pause_threshold = 1
		recognizer.adjust_for_ambient_noise(source, duration=1)
		audio = recognizer.listen(source)
	try:
		text = recognizer.recognize_google(audio, language="ru-RU")
		print(f"Вы сказали: {text}")
	except sr.UnknownValueError:
		print("Я вас не поняла")
		text = None
	return text


answer = listening()