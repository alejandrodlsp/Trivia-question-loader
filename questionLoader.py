###################################################
#	Alejandro de los Santos Puerto
#	alejandrodlsp.com
###################################################

import requests
import json

# Current session token, 0 if nil
session_token = 0


#
# requests data from API and returns it as a string
def request_data(amount, category, difficulty, question_type):
	if session_token == 0 or session_token == None:
		get_session()

	url = "https://opentdb.com/api.php?amount=" + amount + "&category=" + category + "&difficulty=" + difficulty + "&type=" + question_type + "&token=" + str(session_token)
	response = requests.get(url=url)
	data = response.text
	return data


#
# requests a session to the opentdb API and saves it
def get_session():
	url = "https://opentdb.com/api_token.php?command=request"	# API token request url
	response = requests.get(url = url)
	data = json.loads(response.text)

	# parse response code
	if data["response_code"] == 0:
		session_token = data["token"]
		print("Session token: " + str(session_token) + "\n")
	else:
		show_error("Session error", "Could not retrieve a session token")


#
# shows an error message
def show_error(title, error):
	print(title + " : " + error)
	sys.exit()



###
# question set class
class question_set():

	#
	# class constructor
	def __init__(self, amount, category, difficulty, question_type):
		while True:
			self.data = request_data(amount, category, difficulty, question_type)	# request data to api
			self.__dict__ = json.loads(self.data)									# deserialize raw json data into itself

			if self.response_code == 1:												# parse response code
				show_error("No Results", "Request could not return results")
			elif self.response_code == 2:
				show_error("Invalid Parameter", "Request contains an invalid parameter")
			elif self.response_code == 3:
				show_error("Token Not Found", "Request session token could not be found, attempting to find another session")
				get_session()
			elif self.response_code == 4:
				show_error("Empty Session error", "Session is empty, attempting to find another session")
				get_session()
			elif self.response_code == 0:
				break

		# save request serialized results
		self.set = self.Results


	#
	# returns a list of the question objects
	def get(self):
		questions = []
		# loop through all the request result objects and create a question object out of each one
		for i in range(0,len(self.set)):
			question_text = self.set[i]["question"]
			correct_answer = self.set[i]["correct_answer"]
			incorrect_answers = self.set[i]["incorrect_answers"]
			
			qs = question(question_text, correct_answer, incorrect_answers)
			questions.append(qs)

		#return the list of question objects
		return questions



###
# question class
class question():
	def __init__(self, question, correct_answer, incorrect_answers):
		self.question = question
		self.correct_answer = correct_answer
		self.incorrect_answers = incorrect_answers
