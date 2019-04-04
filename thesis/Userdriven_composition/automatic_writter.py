def actuator_function_writter(function_name,url):
	print("writting actuator_function_writter")
	file = open("test_file.py","a+")

	code = """
def """ + function_name+"""(motor_status):
	url = '"""+url+"""'

	data = {

		"topic": """+function_name+""",
		"value": motor_status,
		"time": "2019-01-24T13:35:24.246226Z",
		"name": "1"
        }



	#Call REST API
	response = requests.put(url, data=data)

	#Print Response
	print(response.text)

	"""

	file.write(code)

	file.close()







def sensor_function_writter(function_name,url):
	file = open("test_file.py","a+")

	code = """
def """+function_name+"""():
	empty_list=[]
	sensor_tag = """+function_name+"""
	data = requests.get("http://127.0.0.1:8000/api/lowersensors/").json()
	for i in data:
		if i['topic']==sensor_tag:
			empty_list.append(i)

	data = empty_list[-1]
	print(data)

	data = int(data['value'])
	return(data)
"""

	file.write(code)

	file.close()
