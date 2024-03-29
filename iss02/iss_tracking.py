import urllib.request
import json
## Trace the ISS - earth-orbital space station
eoss = 'http://api.open-notify.org/iss-now.json'

## Call the webserv
trackiss = urllib.request.urlopen(eoss)

## put into file object
ztrack = trackiss.read()

## json 2 python data structure
result = json.loads(ztrack.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(result)
input('\nISS data retrieved & converted. Press any key to continue')    

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('\nLatitude: ', lat)
print('Longitude: ', lon)


