#import requests library for making REST calls
import requests
import json


def action_motor(motor_status):
	url = 'http://127.0.0.1:8000/api/actuators/9/'

	data = {

		"topic": "mc101",
		"value": motor_status,
		"time": "2019-01-24T13:35:24.246226Z",
		"name": "1"
	        }

	

	#Call REST API
	response = requests.put(url, data=data)

	#Print Response
	print(response.text)


def get_lowersensor():
	data = requests.get("http://127.0.0.1:8000/api/lowersensors/2/").json()
	data = int(data['value'])
	return(data)




def value_to_print(text):
	print(text+" pass function")
	return text


def print_content(what_to_print):
	what_to_print=what_to_print+" print_content"
	print(what_to_print)
