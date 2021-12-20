import json

with open("static/data/apt_with_coord_price.json", "r") as f:
    apt=json.load(f)


geojson_dict= {'type':'FeatureCollection','features':[]}

for i in range(315):
    feature_dict = {"type": "Feature", "geometry": {"type": "Point", "coordinates": []},
                    "properties": {"address":"","popup":"","num":0}}
    feature_dict['geometry']['coordinates']=[float(apt["coordinate"][i]['lng']),float(apt['coordinate'][i]['lat'])]
    name=apt['name'][i]
    address=apt['address'][i]
    feature_dict['properties']['address']=address
    url=apt['url'][i]
    price=str(min(apt['floor_plans'][i]['price_range']))+'-'+str(max(apt['floor_plans'][i]['price_range']))
    feature_dict['properties']['popup']=f'<a href="{url}">{name}</a><p>price:{price}</p><p>{address}</p>'
    feature_dict['properties']['num']=i
    geojson_dict["features"].append(feature_dict)

with open("static/data/apt_geojson.geojson", "w") as f:
    json.dump(geojson_dict,f)


