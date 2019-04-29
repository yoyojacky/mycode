import urllib.request
import urllib.parse
import ssl
import json

context = ssl._create_unverified_context()
api = 'https://restapi.amap.com/v3/weather/weatherInfo?key=857e115ce98e9a5c5b93b0289715fe80&city=310000&extensions=base&output=JSON'

req = urllib.request.Request(api)
with urllib.request.urlopen(req, context=context) as response:
    html = response.read().decode()
    js = json.loads(html)
    weather = js['lives'][0]
    for k, v in weather.items():
        print(k,v)
