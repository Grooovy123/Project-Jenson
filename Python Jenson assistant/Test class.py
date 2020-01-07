from datetime import datetime
from datetime import date
import datetime 
import time

import pyttsx3
import speech_recognition as sr
import wikipedia
from mutagen.mp3 import MP3
import os
from pygame import mixer

music_folder = " "
single = "\\"
doub = "\\\\"
file = "C:\\Users\\yolic\\OneDrive\\Desktop\\Music"
file_exists = False

func_num = 10

hello = "Hello world"
print(hello[-1:])
quit()

inp = input("set volume: ")

mixer.init()
mixer.music.set_volume(0.50)

def music_volume_control(func_num, inp):
	print(f"volume is:{mixer.music.get_volume()}")
	if func_num == 10:			
		volume = mixer.music.get_volume()

		if "up" in inp:
			volume += 0.10
		elif "down" in inp:
			volume -= 0.10
		elif "%" == inp[-1:]:
			try:
				volume = int(inp[len(inp)-4:-1])/100				
			except Exception as e:
				volume = int(inp[len(inp)-3:-1])/100
		else:
			print("Error setting volume")			
					
		mixer.music.set_volume(volume)

		if mixer.music.get_volume() < 0.10:
			mixer.music.set_volume(0.10)
		elif mixer.music.get_volume() > 1.0:
			mixer.music.set_volume(1.0)

		print(f"volume is:{mixer.music.get_volume()}")

while True:
	music_volume_control(func_num, inp)
	inp = input("set volume: ")

# try:
# 	if music_folder != "":
# 		if os.path.exists(music_folder):
# 			print(f"True")
# 	else:
# 		print(f"Sorry no such folder exists or the path is no longer valid")
# 		music_folder = str(input("Please enter the path to your music folder: "))
# 		music_folder = music_folder.replace(single, doub)		
# 		print(music_folder)

# except Exception as e:
# 	print(e)

# if os.path.exists(music_folder):
# 	print("hello")
# else:
# 	print("file error")

def does_music_folder_exist(music_folder):		
	if os.path.exists(music_folder):		
		return music_folder
	else:		
		print(f"Sorry no such folder exists or the path is no longer valid")		
		music_folder = str(input("Please enter the path to your music folder: ")).replace("\\\\", "\\")		
		return music_folder

# while file_exists == False:
# 	music_folder = does_music_folder_exist(music_folder, file_exists)
# 	print(f"this is the real file: {file}")
# 	print(f"this is not working: {music_folder}")
# 	if music_folder == file:
# 		print(f"strings are the same")
# 		break

# does_music_folder_exist(music_folder, file_exists)
# does_music_folder_exist(music_folder, file_exists)




music = []
i = 0
if os.path.exists(file):
	music = [song for song in os.listdir(file) if ".mp3" in song]
	for song in music:
		print(song)
	time.sleep(3)
	# for song in os.listdir(file):
		# if ".webm" in song or ".wav" in song:
		# 	pass
		# else:
		# 	music.append("C:\\Users\\yolic\\OneDrive\\Desktop\\Music\\"+song)

def set_up():
	mixer.init()

def load_song(music, i):
	try:
		mixer.music.load(file+"\\"+music[0])
	except Exception as e:		
		mixer.music.load(file+"\\"+music[1])
		raise e
	

def play(music, i):
	mixer.music.load(file+"\\"+music[i])
	mixer.music.play()
	mixer.music.set_volume(.8)
	song = music[i].replace(file+"\\", " ")
	song = song.split("(")
	print(f"now playing{song[0]}")

def stop():
	mixer.music.stop()

set_up()
#load_song(music, i)
play(music, i)
#pygame.mixer.music.set_volume(.5)
print(f"volume: {mixer.music.get_volume()}")
inp = input("Press enter to skip song")

while i <= len(music)-1:
	if inp.lower() == "skip" or inp.lower() == "":
		if i == len(music)-1:
			i = 0
			play(music, i)
		else:
			i += 1		
			play(music, i)
		
	elif inp.lower() == "stop":	
		stop()
	inp = input("Press enter to skip song")

	


#stop()

# music = []
# music_folder = "C:\\Users\\yolic\\OneDrive\\Desktop\\Music"
# if os.path.exists(music_folder):
# 	for song in os.listdir(music_folder):
# 		music.append(song)

# song_len = MP3(f"C:\\Users\\yolic\\OneDrive\\Desktop\\Music\\{music[7]}")

# mins = str(song_len.info.length/60).split(".")[0]
# seconds = str(song_len.info.length/60).split(".")[1][:2]
# print(f"Song is {music[7]}")
# print(f"Song length is: {mins} mins and {seconds} seconds")
# print(f"Uncut song length is {song_len.info.length}")#



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













