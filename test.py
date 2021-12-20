import json

def get_length():
    with open("static/data/apt_with_coord_price.json","r") as f:
        apt=json.load(f)

    apt_length=[]

    for house in apt['floor_plans']:
        apt_len=len(house['price_range'])
        apt_length.append(apt_len)

    print(max(apt_length))

 
