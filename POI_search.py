import json
import requests
import os

base_url="https://maps.googleapis.com/maps/api/place/nearbysearch/json"
parameters=dict.fromkeys(("location","radius","type","key"))
parameters["key"]=""
parameters["radius"]=800
search_type=["gym","restaurant","store"]



with open("static/data/coordinates.json","r") as f:
    coor=json.load(f)

coor["gym"]=[]
coor["restaurant"]=[]
coor["store"]=[]


for type in search_type:
    for coord in coor["coordinate"]:
        parameters['location']=str(coord["lat"])+","+str(coord["lng"])
        parameters["type"]=type
        result=json.loads(requests.request("get",base_url,params=parameters).text)
        coor[type].append(len(result["results"]))
        print(coord)
    print(type)

with open("static/data/poi.json", "w+") as f:
    json.dump(coor,f)




