import requests
import base64
from flask import Flask
import os


# > "asdf==" | base64 --decode

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'tlci0GhK8n5A18K1GTx6KPwfYjuuftWw')


url = "http://178.62.70.56:30935/"

def Base64Encode(s: str):
	return base64.b64encode((s).encode('ascii')).decode('ascii')

def Payload(var: str, stmt: str):
	return {
		"ingredient": var,
		"measurements": stmt
	}
	
def MakeCookie(var: str, stmt: str):
	return {'session': Payload(var, stmt)}

with requests.Session() as s:
	r = s.get(url, cookies=Payload("foo", "100 + 100 + 100"),headers={'Connection': 'keep-alive'})
	print(r.text)
	print(r.headers)
	print(r.cookies)