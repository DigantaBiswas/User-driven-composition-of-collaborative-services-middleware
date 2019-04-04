
	def albert123():
		data = requests.get('localhost').json()
		data = int(data['value'])
		return(data)

	
	def albert000():
		data = requests.get('localhost').json()
		data = int(data['value'])
		return(data)

	
	def albert000():
		data = requests.get('localhost').json()
		data = int(data['value'])
		return(data)

	
	def albert098():
		data = requests.get('localhost').json()
		data = int(data['value'])
		return(data)

	
	def dzbz123():
		data = requests.get('localhost').json()
		data = int(data['value'])
		return(data)

	
	def dzbz123():
		empty_list=[]
		sensor_tag = dzbz123
		data = requests.get("http://127.0.0.1:8000/api/lowersensors/").json()
		for i in data:
			if i['topic']==sensor_tag:
				empty_list.append(i)

		data = empty_list[-1]
		print(data)

		data = int(data['value'])
		return(data)
	
	def voda():
		empty_list=[]
		sensor_tag = voda
		data = requests.get("http://127.0.0.1:8000/api/lowersensors/").json()
		for i in data:
			if i['topic']==sensor_tag:
				empty_list.append(i)

		data = empty_list[-1]
		print(data)

		data = int(data['value'])
		return(data)
	
	def paglachulkene():
		empty_list=[]
		sensor_tag = paglachulkene
		data = requests.get("http://127.0.0.1:8000/api/lowersensors/").json()
		for i in data:
			if i['topic']==sensor_tag:
				empty_list.append(i)

		data = empty_list[-1]
		print(data)

		data = int(data['value'])
		return(data)
	
	def arif+gay+mozahid():
		empty_list=[]
		sensor_tag = arif+gay+mozahid
		data = requests.get("http://127.0.0.1:8000/api/lowersensors/").json()
		for i in data:
			if i['topic']==sensor_tag:
				empty_list.append(i)

		data = empty_list[-1]
		print(data)

		data = int(data['value'])
		return(data)
	
	def arifmagirchele():
		empty_list=[]
		sensor_tag = arifmagirchele
		data = requests.get("http://127.0.0.1:8000/api/lowersensors/").json()
		for i in data:
			if i['topic']==sensor_tag:
				empty_list.append(i)

		data = empty_list[-1]
		print(data)

		data = int(data['value'])
		return(data)
	
	def tomarbara():
		empty_list=[]
		sensor_tag = tomarbara
		data = requests.get("http://127.0.0.1:8000/api/lowersensors/").json()
		for i in data:
			if i['topic']==sensor_tag:
				empty_list.append(i)

		data = empty_list[-1]
		print(data)

		data = int(data['value'])
		return(data)
	
defasholbara(motor_status):
	url = 'localhost'

	data = {

		"topic": asholbara,
		"value": motor_status,
		"time": "2019-01-24T13:35:24.246226Z",
		"name": "1"
        }



	#Call REST API
	response = requests.put(url, data=data)

	#Print Response
	print(response.text)

	
defhazabaeala(motor_status):
	url = 'dfdf'

	data = {

		"topic": hazabaeala,
		"value": motor_status,
		"time": "2019-01-24T13:35:24.246226Z",
		"name": "1"
        }



	#Call REST API
	response = requests.put(url, data=data)

	#Print Response
	print(response.text)

	