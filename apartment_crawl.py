import os
import requests
from bs4 import BeautifulSoup
import time
import json
import re
from pathlib import Path

current_path = os.path.abspath(__file__)
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

def fetch_url(url, **kwargs):
    '''
    This funcion is to see if the content of the page can be fetched successfully rather than fetching the error
    :param url: The url of webpage
    :return: the webpage of the url in normal situation, or report the error
    '''
    url = str(url)
    while True:
        try:
            r = requests.get(url,**kwargs)
            while r.text.strip() == '':
                print('the result is null, redo')
                print(r.text)
            return r
        except TimeoutError as e:
            print(url)
            print(e)
            print('TimeoutError')
            os.system("pause")
        except Exception as e:
            print(url)
            print(e)
            print('Something wrong')
            os.system("pause")
headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Proxy-Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

def get_photo_url(house):
    try:
        style=str(house.find('div',class_="item active").get("style"))
        if style == 'None':
            style=str(house.find('div',class_="item active").get("data-image"))
            return style
        pattern=re.compile(r'\((.+?)\)')
        url=pattern.search(style).group(0)
        url=re.sub(r'[\(\"\"\)\;]',"",url)
        return url
    except Exception as e:
        print(e)
        return "no data"
url="https://www.apartments.com/ann-arbor-mi/"
r=fetch_url(url,timeout=10,headers=headers)

apt_bs=BeautifulSoup(r.content,"html.parser")

page=apt_bs.find('span',class_='pageRange').text.split(sep=" ")

start_page=int(page[1])
end_page=int(page[3])+1

file_path=Path("apartments.json")
if file_path.exists():
    with open(file_path,'r') as f:
        attr_dic=json.load(f)
else:
    keys=['name', 'address', 'floor_plans', 'url', 'photo', 'amenities', 'features']
    attr_dic = dict([(k,[]) for k in keys])


for page in range(start_page,end_page):
    r=fetch_url((url+"/"+str(page)+"/"),headers=headers,timeout=10)
    bs=BeautifulSoup(r.content,"html.parser")
    house_list=bs.find('div', id='placardContainer').find_all('li',class_="mortar-wrapper")
    if house_list is not None:
        for house in house_list:
            if house.find(class_="js-placardTitle title") is not None:
                if house.find(class_='property-address js-url').get("title") in attr_dic['address']:
                    continue
            if house.find(class_="js-placardTitle title") is not None:
                attr_dic['name'].append(house.find(class_="js-placardTitle title").text)
            else:
                attr_dic['name'].append("no data")
            if house.find(class_="property-address js-url") is not None:
                attr_dic['address'].append(house.find(class_="property-address js-url").get("title"))
            else:
                attr_dic['address'].append("no data")
            if house.find(class_='property-link') is not None:
                house_url=house.find(class_='property-link').get('href')
                attr_dic['url'].append(house_url)

            attr_dic['photo'].append(get_photo_url(house))

            house_info=BeautifulSoup(fetch_url(house_url,headers=headers,timeout=10).content,'html.parser')
            if house_info.select('div[data-tab-content-id=\'all\']') is not None:
                floor_plan_list=house_info.select('div[data-tab-content-id=\'all\']')[0].find_all(class_=re.compile(r'pricingGridItem'))
                if floor_plan_list is not None:
                    key_dict=["price_range","floor_name","floor_type"]
                    d1=dict([(k,[]) for k in key_dict])
                    for floor_plan in floor_plan_list:
                        price_range=floor_plan.find(class_="rentLabel").text.strip()
                        floor_name=floor_plan.find(class_="modelName").text.strip()
                        pattern=re.compile(r'\s+')
                        floor_type=re.sub(pattern,'',floor_plan.find(class_="detailsTextWrapper").text.strip())
                        d1["price_range"].append(price_range)
                        d1["floor_name"].append(floor_name)
                        d1["floor_type"].append(floor_type)
                    attr_dic['floor_plans'].append(d1)

            else:
                d1["price_range"].append("no data")
                d1["floor_name"].append("no data")
                d1["floor_type"].append("no data")
                attr_dic['floor_plans'].append(d1)

            if house.find(class_="property-amenities") is not None:
                amenities=house.find(class_="property-amenities").find_all("span")
                amenity_str=str()
                for amenity in amenities:
                    amenity_str=amenity_str+amenity.text+","
                attr_dic['amenities'].append(amenity_str)
            else:
                attr_dic['amenities'].append("no data")
            print("page ",page,"house",len(attr_dic['name']),"finished")
            time.sleep(1)


    else:
        print("page"+page+" is something wrong")
    with open(file_path,"w+") as f:
        json.dump(attr_dic,f)
    print("page",page,"finished",sep=" ")
    time.sleep(0.5)

















