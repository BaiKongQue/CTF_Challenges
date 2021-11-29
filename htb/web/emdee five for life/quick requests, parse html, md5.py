import requests
import hashlib
from HTMLParser import HTMLParser

url = "http://ip:port/"

s = requests.Session()

r = s.post(url, {
	"hash": 'asdf'
})

print(r.text)

class Parser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.foo = []
		
	def handle_starttag(self, tag, attrs):
		if (tag == 'h3'):
			self.foo.append(tag)
			
	def handle_endtag(self, tag):
		if (tag == 'h3'):
			self.foo.pop()
			
	def handle_data(self, data):
		if (self.foo):
			h = hashlib.md5(data).hexdigest()
			rr = s.post(url, {
				"hash": h
			})
			print(rr.text)

p = Parser()
p.feed(r.text)


# OTHER SOLUTION TO PARSE #
import re

def strip_tags(html):
	clean = re.compile('<.*?>')
	return re.sub(clean, '', html)

out1 = html_tags(r.text)
out2 = out1.split('string')[1] 	# split input of "...string12345" where string is delimiter between stuff and string to hash
out3 = out2.rstrip()

s.close()