## [In Progress] ##

# Exploratory Phase #
The web page is very simple and does not have a lot of information to work with.

one of the things I found that could be exploited is a cookie called `session` that holds base64 encoded data separted into 3 parts by a `.`:
```
eyJpbmdyZWRpZW50Ijp7IiBiIjoiWjNwbWJtVjFlV04zZHc9PSJ9LCJtZWFzdXJlbWVudHMiOnsiIGIiOiJNVEV0TlRNPSJ9fQ.YJckTQ.4-QFL78wdMOipUhdVzutRM830_0
```

## Session Cookie ##
When the data is decoded it contains the following:

[eyJpbmdyZWRpZW50Ijp7IiBiIjoiWjNwbWJtVjFlV04zZHc9PSJ9LCJtZWFzdXJlbWVudHMiOnsiIGIiOiJNVEV0TlRNPSJ9fQ]
```json
{"ingredient":{" b":"Z3pmbmV1eWN3dw=="},"measurements":{" b":"MTEtNTM="}}
```
`YJckTQ`
```json
`$M
```
`4-QFL78wdMOipUhdVzutRM830_0`
```json
4-@RL:*TsL}?
```

The first portion of the data seems to be JSON with more base64 encoded data.
Once fully decoded I got the following:
```JSON
{
	"ingredient": {
		" b": "gzfneuycww"
	},
	"measurements": {
		" b": "11-53"
	}
}
```

The `measurements['b']` seems to be the calculation for the number shown on the website.

Unfortunately the session cookie changes each time the page is reloaded, meaning the session cookie is probably only used after it is set. Hard to tell right now but I will keep this in mind just in case.

## OWASP DirBuster ##
Not seeing much else, I decided to run DirBuster with the `common.txt` from `/usr/share/dirb/wordlist/`

One result it found was a `/webservice.php` file and a `/debug` directory.

going to `ip:port/debug`resulted in the following python code:
```py
from flask import Flask, Response, session, render_template
import functools, random, string, os, re

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'tlci0GhK8n5A18K1GTx6KPwfYjuuftWw')

def calc(recipe):
    global garage
    builtins, garage = {'__builtins__': None}, {}
    try: exec(recipe, builtins, garage)
    except: pass

def GFW(func): # Great Firewall of the observable universe and it's infinite timelines
    @functools.wraps(func)
    def federation(*args, **kwargs):
        ingredient = session.get('ingredient', None)
        measurements = session.get('measurements', None)

        recipe = '%s = %s' % (ingredient, measurements)
        if ingredient and measurements and len(recipe) >= 20:
            regex = re.compile('|'.join(map(re.escape, ['[', '(', '_', '.'])))
            matches = regex.findall(recipe)
            
            if matches: 
                return render_template('index.html', blacklisted='Morty you dumbass: ' + ', '.join(set(matches)))
            
            if len(recipe) > 300: 
                return func(*args, **kwargs) # ionic defibulizer can't handle more bytes than that
            
            calc(recipe)
            # return render_template('index.html', calculations=garage[ingredient])
            return func(*args, **kwargs) # rick deterrent

        ingredient = session['ingredient'] = ''.join(random.choice(string.lowercase) for _ in xrange(10))
        measurements = session['measurements'] = ''.join(map(str, [random.randint(1, 69), random.choice(['+', '-', '*']), random.randint(1,69)]))

        calc('%s = %s' % (ingredient, measurements))
        return render_template('index.html', calculations=garage[ingredient])
    return federation

@app.route('/')
@GFW
def index():
    return render_template('index.html')
 
@app.route('/debug')
def debug():
    return Response(open(__file__).read(), mimetype='text/plain')

if __name__ == '__main__':
    app.run('0.0.0.0', port=1337)
```

## /debug ##
After examining the code I have realized that the `session` cookie is being used and ran before it issues a new one. From that I also learned that there was a vulnerability that can be exploited by this.

I noticed the code utilizes the `ingedient` and `measurements` parts of the cookies which gets put into a string which is then ran with a `exec(...)` where `garage` holds the results, and `ingredient` is the key to get the result from that `exec()`. These are then returned to the page via `calculations=garage[ingredient]`.

# Infiltration #
