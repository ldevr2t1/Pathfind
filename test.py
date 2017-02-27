import json
import requests

if __name__ == '__main__':
	address = 'localhost:8080';
	uid = 3;
	test_data = {'testint': 3, 'teststring': 'hi', 'testobj': {'inside': True}}
	response = requests.get('http://' + address + '/v1/' + str(uid))
	print (response.status_code);
	print (response);
	response = requests.delete('http://' + address + '/v1/' + str(uid))
	print (response.status_code);
	print (response.json());
	#assert response.status_code == 200
	response = requests.get('http://' + address + '/v1/' + str(uid))
	print (response.status_code);
	print (response.json());
	#assert response.status_code == 404