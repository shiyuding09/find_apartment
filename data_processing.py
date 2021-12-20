import json

# with open("apt_coord_price_poi.json") as f:
#     apt=json.load(f)
#
# for i in range(315):
#     house=apt["floor_plans"][i]
#     price_range=house['price_range']
#     house_type=house['floor_type']
#     new_price_range=[]
#     for price in price_range:
#         if (price.find(' ') != -1):
#             price=price.split(' ')
#             price=price[0]
#         price=price.strip().replace("$","").replace(",","")
#         if price=="Call":
#             price=0
#         new_price_range.append(int(price))
#
#     apt['floor_plans'][i]['price_range']=new_price_range
#
#
#
# with open("apt_with_coord_price.json","w") as f:
#     json.dump(apt,f)

def split_house_type():
    with open("static/data/apt_coord_price_poi.json","r") as f:
        apt = json.load(f)
    for i in range(315):
        for j in range(apt['house_type'][i]):
            floor=apt['floor_plans'][i]['floor_type'][j].split(",",2)
            bed=floor[0]
            bath=floor[1]
            apt['floor_plans'][i]['floor_type'][j]={"bed":bed,"bath":bath}
    return apt

if __name__=='__main__':
    apt=split_house_type()
    with open("static/data/apt_floor_split.json", "w") as f:
        json.dump(apt,f)


