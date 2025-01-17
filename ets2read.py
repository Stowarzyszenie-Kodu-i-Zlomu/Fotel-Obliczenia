import json
from urllib.request import urlopen

# GET http://localhost:25555/api/ets2/telemetry

#Odczytaj wartości z JSON'a

url = "http://localhost:25555/api/ets2/telemetry"
respond = urlopen(url)
dataJson = json.loads(respond.read())

print(dataJson)

placement = dataJson.get('placement')

print(placement)

pitch = placement['pitch']
roll = placement['roll']

print("Pitch: ", pitch)
print("Roll: ", roll)
