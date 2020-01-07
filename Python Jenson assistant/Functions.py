import time
from datetime import datetime
from datetime import date
import datetime
from JENSON_MAIN import *
import requests
import webbrowser
import wikipedia
import os 
from pygame import mixer
from random import shuffle

class Function():
	def __init__(self):
		self.days_of_week = {
		0:"Monday",
		1:"Tuesday",
		2:"Wednesday",
		3:"Thursday",
		4:"Friday",
		5:"Saturday",
		6:"Sunday"
		}
		self.music_folder = " "#C:\\Users\\yolic\\OneDrive\\Desktop\\Music
		self.music_folder_valid = False
		self.music_list = []

		mixer.init()
		mixer.music.set_volume(0.5)

		self.song_num = 0
		self.play_music_now = False			

	### GETS THE CURRENT TIME ###
	def get_time(self, func_num):
		if func_num == 0:
			hour = int(datetime.datetime.now().hour)
			mins = int(datetime.datetime.now().minute)

			if hour == 0:
				hour = 12
			elif hour > 12:
				hour = hour - 12				
				return print(f"The time is: {hour}:{mins}pm")
			return print(f"The time is: {hour}:{mins}am")

	### GETS THE CURRENT DAY###
	def get_day(self, func_num):
		if func_num == 1:								
			return print(f"Today is: {self.days_of_week[date.today().weekday()]}")		

	### REMOVE OLD MODEL ###
	def remove_model(self, func_num):
		if func_num == 2:			
			os.remove("model.tflearn.data-00000-of-00001")
			os.remove("model.tflearn.meta")
			os.remove("model.tflearn.index")

			self.retrain_jenson(func_num)			

	### RETRAIN MODEL AND UPDATE INTENTS ###
	def retrain_jenson(self, func_num):
		if func_num == 2:
			try:				
				print(f"retraining beginning")
				data = read_JSON()				
				words, labels, training, output = intents_prep(data)				
				model = DNN(training, output, True)				
				train(model, training, output)				
				print(f"retraining complete")
				return model, words, labels, data 			
			except Exception as e:
				print(e)

	### CREATES A TIDY QUERY FOR WEB SEARCH ###
	def get_query_for_web(self, func_num, query, data):
		if func_num == 3:			
			for tag in data["intents"]:
				if tag['tag'] == "search":
					patterns = tag['patterns']
					for i in range(len(patterns)):													
						if patterns[i] in query:
							query = query.replace(patterns[i]+" ", "")									
							self.search_web(func_num, query)							

	### SEARCHES WEB FOR QUERY ###
	def search_web(self,func_num, query):
		if func_num == 3:			
			url = f"https://www.google.com/search?q={query}"
			webbrowser.open(url)

			return print(f"Searching web for {query}")

	### TEST ###
	def test(self, func_num):
		if func_num == 4:			
			return print(f"WTF IS GOING ON")		

	### WIKI SEARCH FOR QUESTIONS ###
	def Wiki_search(self, func_num, query):
		if func_num == 5:
			try:
				print(f"Searching wiki: {query}")
				start_time = time.time()
				reaults = wikipedia.summary(query, sentences=2)
				print(f"Time took: {time.time() - start_time} seconds")	
				return f"Acording to wikipedia {reaults}"			
			except Exception as e:
				return e			

	### OPEN WEB BROWSER TO SPECIFIC SITE ###
	def open_browsers(self, func_num, query):
		if func_num == 6:
			try:
				query = query.split()
				webbrowser.open(f"https://www.{query[1]}.com")
				return print(f"{query[1]} is now open")
			except Exception as e:				
				return print(e)

			#####	MUSIC 	#####

	### SETUP MUSIC FOLDER LOCATION ###
	def does_music_folder_exist(self, func_num):
		if func_num == 9:
			if self.play_music_now == True:
				self.play_music(func_num)
			else:
				while self.music_folder_valid == False:		
					if os.path.exists(self.music_folder):
						self.music_folder_valid = True
						self.play_music_now = True
						self.load_music()						

					else:		
						print(f"Sorry no such path exists or the path is no longer valid")		
						self.music_folder = str(input("Please enter the path to your music folder: ")).replace("\\\\", "\\")

	### STORE MUSIC IN FOLDER TO LIST ###			
	def load_music(self):
		if self.music_folder_valid == True:			
			if os.path.exists(self.music_folder):
				self.music_list = [song for song in os.listdir(self.music_folder) if ".mp3" in song]
				shuffle(self.music_list)				
				self.load_song()
				print(len(self.music_list))				
			else:
				self.does_music_folder_exist(func_num)

	### LOAD SONG READY TO PLAY ###
	def load_song(self):
		if self.music_folder_valid == True:
			if self.song_num == len(self.music_list)-1:
				self.song_num = 0
				self.shuffle_music(12)				
			else:				
				self.song_num += 1

			print(self.song_num)

			mixer.music.load(self.music_folder+"\\"+self.music_list[self.song_num])

	### SHUFFLES MUSIC LIST ###		
	def shuffle_music(self, func_num):
		if func_num == 12:
			shuffle(self.music_list)		
			
	### PLAY MUSIC ###
	def play_music(self, func_num):
		if func_num == 7:
			if self.play_music_now == True:			
				mixer.music.play()
				print("Music is playing")
			else:				
				self.does_music_folder_exist(9)
				self.play_music(7)			

	### STOP MUSIC ###
	def stop_music(self, func_num):
		if func_num == 8:
			if mixer.music.get_busy() == True:			
				mixer.music.stop()

	### SKIP SONG PLAYS NEXT SONG IN THE LIST ###
	def skip_song(self, func_num):
		if func_num == 10:			
			self.load_song()			
			self.play_music(7)

	### VOLUME CONTROL FOR MUSIC ###
	def music_volume_control(self, func_num, inp):
		if func_num == 11:			
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






			
			
			
			



		
	



