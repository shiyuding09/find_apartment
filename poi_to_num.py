import json

with open("static/data/poi.json","r") as f:
    poi=json.load(f)

with open("static/data/apt_with_coord_price.json","r") as f:
    apt=json.load(f)

apt["gym"]=[len(gym) for gym in poi['gym']]
apt["restaurant"]=[len(restaurant) for restaurant in poi['restaurant']]
apt["store"]=[len(store) for store in poi["store"]]

with open("static/data/apt_coord_price_poi.json","w") as f:
    json.dump(apt,f)