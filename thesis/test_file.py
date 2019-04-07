

def kihdis1():
	empty_list=[]
	sensor_tag = kihdis1
	data = requests.get("http://192.168.1.137:8000/api/lowersensors/").json()
	for i in data:
		if i['topic']==sensor_tag:
			empty_list.append(i)

	data = empty_list[-1]
	print(data)

	data = int(data['value'])
	return(data)

def soil_moisture_sensor::3.22::1.22::Digonta3():
	empty_list=[]
	sensor_tag = soil_moisture_sensor::3.22::1.22::Digonta3
	data = requests.get("http://192.168.1.137:8000/api/lowersensors/").json()
	for i in data:
		if i['topic']==sensor_tag:
			empty_list.append(i)

	data = empty_list[-1]
	print(data)

	data = int(data['value'])
	return(data)

def soil_moisture_sensor_3.22_1.22_Avee4():
	empty_list=[]
	sensor_tag = soil_moisture_sensor_3.22_1.22_Avee4
	data = requests.get("http://192.168.1.137:8000/api/lowersensors/").json()
	for i in data:
		if i['topic']==sensor_tag:
			empty_list.append(i)

	data = empty_list[-1]
	print(data)

	data = int(data['value'])
	return(data)

def soil_moisture_sensor_2_33_1_22_Arif5():
	empty_list=[]
	sensor_tag = soil_moisture_sensor_2_33_1_22_Arif5
	data = requests.get("http://192.168.1.137:8000/api/lowersensors/").json()
	for i in data:
		if i['topic']==sensor_tag:
			empty_list.append(i)

	data = empty_list[-1]
	print(data)

	data = int(data['value'])
	return(data)

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
	response = requests.put(url, data=data)

	#Print Response
	print(response.text)

	
def Motor_actuator_longi_actuator_lati_User(motor_status):
	url = 'http://192.168.1.137:8000/api/actuators/'

	data = {

		"topic": 'Motor_actuator_longi_actuator_lati_User',
		"value": motor_status,
		"time": "2019-01-24T13:35:24.246226Z",
		"name": "1"
        }



	#Call REST API
	response = requests.put(url, data=data)

	#Print Response
	print(response.text)

	
def Motor_actuator_longi_actuator_lati_New User(motor_status):
	url = 'http://192.168.1.137:8000/api/actuators/'

	data = {

		"topic": 'Motor_actuator_longi_actuator_lati_New User',
		"value": motor_status,
		"time": "2019-01-24T13:35:24.246226Z",
		"name": "1"
        }



	#Call REST API
	response = requests.put(url, data=data)

	#Print Response
	print(response.text)

	