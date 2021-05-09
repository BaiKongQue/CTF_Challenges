# Exploratory Phase #
The web page is very simple and does not have a lot of information to work with.

one of the things I found that could be exploited is a cookie called `session` that holds base64 encoded data separted into 3 parts by a `.`:
```
eyJpbmdyZWRpZW50Ijp7IiBiIjoiWjNwbWJtVjFlV04zZHc9PSJ9LCJtZWFzdXJlbWVudHMiOnsiIGIiOiJNVEV0TlRNPSJ9fQ.YJckTQ.4-QFL78wdMOipUhdVzutRM830_0
```

# Session Cookie #
When the data is decoded it contains the following:
```json
// eyJpbmdyZWRpZW50Ijp7IiBiIjoiWjNwbWJtVjFlV04zZHc9PSJ9LCJtZWFzdXJlbWVudHMiOnsiIGIiOiJNVEV0TlRNPSJ9fQ
{"ingredient":{" b":"Z3pmbmV1eWN3dw=="},"measurements":{" b":"MTEtNTM="}}
```
```json
// YJckTQ
`$M
```
```json
// 4-QFL78wdMOipUhdVzutRM830_0
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

Unfortunately the session cookie changes each time the page is reloaded, meaning the session cookie is probably only used after it is set.
Hard to tell right now but I will keep this in mind for now.

