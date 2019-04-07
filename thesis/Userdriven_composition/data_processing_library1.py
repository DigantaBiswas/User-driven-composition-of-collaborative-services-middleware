#import requests library for making REST calls
import requests
import json




def weather_info(city):
	api_key = "bd27419d66c8678613e978ca561ad3f7"
	url = "http://api.openweathermap.org/data/2.5/forecast?q="+city+"&APPID={}".format(api_key)
	data = requests.get(url).json()

	#data = data['weather']
	#print(data['name'])
	#print(json.dumps(data, indent = 4, sort_keys=True))

	data=(data['list'][0]['main']['temp'])
	print(data)
	return data






def action_motor(motor_status):
	url = 'http://192.168.1.137:8000/api/actuators/9/'

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
	empty_list=[]
	sensor_tag = 'soil_moisture_sensor::2.33::21.22::sayeed'
	data = requests.get("http://192.168.1.137:8000/api/lowersensors/").json()
	for i in data:
		if i['topic']==sensor_tag:
			empty_list.append(i)

	data = empty_list[-1]
	print(data)

	data = int(data['value'])
	return(data)




def value_to_print(text):
	print(text+" pass function")
	return text


def print_content(what_to_print):
	what_to_print=what_to_print+" print_content"
	print(what_to_print)


def soil_moisture_sensor_2_33_1_22_Arif5():
	empty_list=[]
	sensor_tag = "soil_moisture_sensor_2.33_1.22_Arif"
	data = requests.get("http://192.168.1.137:8000/api/lowersensors/").json()
	for i in data:
		if i['topic']==sensor_tag:
			empty_list.append(i)

	data = empty_list[-1]
	# print(data)

	data = int(data['value'])
	print (data)
	return data

def soil_moisture_sensor_3_22_2_111_User():
	empty_list=[]
	sensor_tag = "soil_moisture_sensor_3.22_2.111_User"
	data = requests.get("http://192.168.1.137:8000/api/lowersensors/").json()
	for i in data:
		if i['topic']==sensor_tag:
			empty_list.append(i)

	data = empty_list[-1]
	print(data)

	data = int(data['value'])
	return(data)


def Motor_actuator_longi_actuator_lati_Sayeed(motor_status):
	url = 'http://192.168.1.137:8000/api/actuators/'

	data = {

		"topic": 'Motor_actuator_longi_actuator_lati_Sayeed',
		"value": motor_status,
		"time": "2019-01-24T13:35:24.246226Z",
		"name": "1"
        }



	#Call REST API
	response = requests.post(url, data=data)

	#Print Response
	print(response.text)