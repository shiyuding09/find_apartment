# What does this project do

This project first provides the method to crawl data from Apartments and parse the data in json format, then converts the address from Apartments.com to coordinates using Google developer API and get the POI(point of interest) near the data from Apartments. Finally it create a web interface to present the house information from Aparments to let people choose their dream apartment.

# Before you start

## Package 

`Beautiful Soup`: To Analyze and parse the HTML that returned by requests.

`Flask`: To create a web app and provide framework.

`re`: To pre-process the information from Apartments and make it more structured.

## JavaScript Library

`JQuery`:Front and back-end data interaction and front-end partial refreshing

`echarts`: To create the bar plot

`leaflet`: To provide Dynamic and interactive maps

# How to use it

To create the final web page of the project, the python file can be divided into 3 parts:Data Obataining, Data processing and make the app.

1. Data Obataining

+ Crawl Apartments

  Firstly, use the python file `apartment_crawl.py`. In this python file, function `fetch_url` is used to get the content from the url and determine if the status code is normal in case of unstable network connection or anti-crawler encounter.
  In this project, `name`, `address`, `floor_plans`, `url`, `photo`, `amenities`, `features` were obatained and stored in dictionary class: `{'name':[],'address'[]}` etc, the same index in each key described the same house.
  This code will create a json file named `apartments.json`
 
 + Geocoding
  Using GOOGLE developer API to geocode the address to coordinate. One import parameters is Goole Developer Api. `geocode_api.py` is the file to geocode. This will generate a dictionary object `{address:[],coordinates:[{lat,lng}]}`
 
 +Nearby POI search
 Using Google developer API to get the nearby poi information. The data from google api is json Format. It contains the location,price and other information with the poi. This file will generate `poi.json` file
 
2. Data Processing
  + Oragnize the crawl data: The raw data of price have several confusion factors like $1,999. To make use of this data, the price must be organized to 1999 format. Also the description of house type is '1bed,2baths,19204squares', which need to be oraganized to {bed:1bed,bath:2baths}. `DataProcessing.py` will generate a new json file with tidy data format.
  + make geojson file: Geojson format will be useful for leaflet to make a map in the front end.`json_to_geojson.py`will make the file with coordrdnate to a geojson Object. 
  
3. create app
  
  In this project，the front end and back end interaction mainly implemented by ajax. Using `Get` and `Post ` methods to calling the back-end routes and acquire the data. Not the best way. Many things can be done in the frone-end. The impletation of the web is in `web.py`. `get_point` functions are used to aquire the data information that is clicked on and return POI data to the front end to create the plot.
  `get_question` function is used to return the question of the question tree. It get the array of answer(Yes is 1 and No is 2) to find the next question.
  
  The implementation of map is totally in the front-end. Use Ajax to get the local geojson and use `leaflet` to make the map.
  
  



