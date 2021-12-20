import json
import requests
import os

current_path = os.path.abspath(__file__)
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

with open("apartments.json",'r') as f:
    apt_dict=json.load(f)

api_key="AIzaSyD7mVOSuBNPWrsqABz28q9n5YCd57_4fzA"
url="https://maps.googleapis.com/maps/api/geocode/json"

parameters=dict.fromkeys(("address","key"))
parameters['key']=api_key
coordinates=[]
for address in apt_dict['address']:
    parameters['address']=address
    google_json=json.loads(requests.get(url,params=parameters).text)
    coord=google_json['results'][0]['geometry']['location']
    coordinates.append(coord)
    print(len(coordinates),"finished",sep=" ")

coord_dict={'address':apt_dict['address'],'coordinate':coordinates}
with open("coordinates.json",'w+') as f:
    json.dump(coord_dict,f)

