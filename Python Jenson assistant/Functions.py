import time
from datetime import datetime
from datetime import date
import datetime
from JENSON_MAIN import *
import requests
import webbrowser
import wikipedia 

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

	### GETS THE CURRENT TIME ###
	def get_time(self, func_num):
		if func_num == 0:
			hour = int(datetime.datetime.now().hour)
			mins = int(datetime.datetime.now().minute)

			if hour == 0:
				hour = 12
			elif hour > 12:
				hour = hour - 12				
				return f"The time i5s: {hour}:{mins}pm"
			return f"The time is: {hour}:{mins}am"

	### GETS THE CURRENT DAY###
	def get_day(self, func_num):
		if func_num == 1:								
			return f"Today is: {self.days_of_week[date.today().weekday()]}"		

	### REMOVE OLD MODEL ###
	def remove_model(self, func_num):
		if func_num == 2:			
			os.remove("model.tflearn.data-00000-of-00001")
			os.remove("model.tflearn.meta")
			os.remove("model.tflearn.index")			

	### RETRAIN MODEL AND UPDATE INTENTS ###
	def retrain_jenson(self, func_num, null, func):
		if func_num == 2:
			try:				
				print(f"retraining beginning")
				data = read_JSON()				
				words, labels, training, output = intents_prep(data)				
				model = DNN(training, output, True)				
				train(model, training, output)				
				print(f"retraining complete")
				chat(model, words, labels, data, func)				
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
												
					return query		

	### SEARCHES WEB FOR QUERY ###
	def search_web(self,func_num, query):
		if func_num == 3:			
			url = f"https://www.google.com/search?q={query}"
			webbrowser.open(url)

			return f"Searching web for {query}"

	### TEST ###
	def test(self, func_num):
		if func_num == 4:			
			return f"WTF IS GOING ON"		

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
				return f"{query[1]} is now open"
			except Exception as e:
				return e
			 

			
			
			
			



		
	



