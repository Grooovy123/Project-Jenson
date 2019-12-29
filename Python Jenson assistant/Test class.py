from datetime import datetime
from datetime import date
import datetime 
import time

import pyttsx3
import speech_recognition as sr
import wikipedia


string = "Hello world"

string = string.split()

print(string[1])
# print("Error")
# print("Error")
# try:
# 	engine = pyttsx3.init('sapi5')
# except Exception as e:
# 	print(e)

# print("Error")
# voices = engine.getProperty('voices')
# print("Error")

# engine.setProperty('voices', voices[0].id)

# def speak(audio):
# 	engine.say(audio)
# 	engine.runandwait()

# def wish_me():
# 	print("Running")
# 	hour = int(datetime.datetime.now().hour)
# 	if hour>=0 and hour<12:
# 		speak('Good morning sir')
# 	else:
# 		speak('Welcome back sir')

# 	speak('How may I help you , sir')

# def take_command():
# 	r = sr.Recognizer()
# 	with sr.Microphone() as source:
# 		print('Listening...')
# 		r.pause_threshold = 1
# 		audio = r.Listen(source)

# 	try:
# 		print('Recognizing...')
# 		query = r.recognize_google(audio, language='en-in')
# 		print(f"You: {query}\n")

# 	except Exception as e:
# 		print(e)
# 		print("Sorry please say that again...")
# 		return query 

# 	return query

# print("Error")
# print("Broken")
# wish_me()
# while True:		
# 	speak("Husbands ask repeated resolved but laughter debating. She end cordial visitor noisier fat subject general picture. ")
# 	query = take_command().lower()

# 	if "wikipedia" in query:
# 		speak("Searching wikipedia")
# 		query = query.replace("wikipedia", "")
# 		reaults = wikipedia.summary(query, sentence=2)
# 		speak("Acording to wikipedia")
# 		print(reaults)
# 		speak(reaults)













