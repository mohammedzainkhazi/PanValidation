import json
import requests

def validatePan(pcno):
	url = "https://31j0q0noye.execute-api.us-east-1.amazonaws.com/hackathon/panverify?pancard="+pcno;
	payload={}
	headers = {}
	response = requests.request("GET", url, headers=headers, data=payload)
	y = response.json()
	if y['validPan'] == 'True':
		print('Congratulations you can proceed!')
	else:
		print('Invalid Pan Number!')