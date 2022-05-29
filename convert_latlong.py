# import requests
# import json
#
#
# x = requests.get('http://api.positionstack.com/v1/forward'
#                  '?access_key=36c9aa06c1546ce9865f48461f0f54dd'
#                  '&query=country=AU')
#
# x_json = json.loads(x.text)
#
# data = x_json['data']
#
# for i in data:
#     print(i)

# API_KEY = 'AIzaSyAeFUrXmW_Y2QoSk5P1SDbZb5hm-cv0rYA'
#
# address = 'Bệnh viện Đa khoa Quốc tế Vinmec Times City'
#
# params = {
#     'key': API_KEY,
#     'address': address
# }
#
# base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
#
# respone = requests.get(base_url, params=params).json()
#
# respone.keys()
#
# print(respone)

# import http.client, urllib.parse, json
#
# conn = http.client.HTTPConnection('api.positionstack.com')
#
# params = urllib.parse.urlencode({
#     'access_key': '36c9aa06c1546ce9865f48461f0f54dd',
#     'query': 'Hà Đông',
#     'county': 'Hà Đông',
#     'region': 'Ha noi',
#     'limit': 80
#     })
#
# conn.request('GET', '/v1/forward?{}'.format(params))
#
# res = conn.getresponse()
# data = res.read()
# data = json.loads(data.decode('utf-8'))
#
# data_json = data['data']
# for i in data_json:
#     print(i)
import csv

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="a")

f = open('data/data_bb6_main.csv', 'a', encoding='utf-8', newline='')
writer = csv.writer(f)

# Total: 84128

min_lat = 20.851
max_lat = 20.899
min_long = 105.671
max_long = 105.910

lat = 20.889
long = 105.854
count = 1

while lat <= max_lat:
    while long <= max_long:
        data = list()
        try:
            location = geolocator.reverse("%s, %s" % (str(lat), str(long)), timeout=10)
            data.append(location.address)
            data.append(str(format(lat, '.3f')))
            data.append(str(format(long, '.3f')))
        except:
            pass

        writer.writerow(data)
        f.flush()
        print(count)
        count += 1

        long += 0.001

    lat += 0.001
    long = min_long

