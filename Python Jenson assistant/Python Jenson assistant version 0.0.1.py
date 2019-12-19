import time
import os
import playsound
import speech_recognition as sr
from gtts import gTTS 


def Speak(text):
	tts = gTTS(text=text, lang='en')
	filename = "voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)
	os.remove(filename)

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""
		try:
			said=r.recognize_google(audio)
			print(said)
		except Exception as e:
			print(f"Exception: {e}")

	return said

Speak("Hello, How may I help you today")
print("awaiting command")
text = get_audio()

if "schedule" in text:
	print("You currently have nothing in your schedule")
	Speak("You currently have nothing in your schedule")
