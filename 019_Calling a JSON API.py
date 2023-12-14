# Calling a JSON API
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps. API End Points

# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

# http://py4e-data.dr-chuck.net/json?

# This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response. To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in

# http://www.py4e.com/code3/geojson.py

# Make sure to check that your code is using the API endpoint as shown above. You will get different results from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.

# Importing the necesarry files and methods

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json

# Ignoring SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False
# api_key = "Google's API key"
# https://developers.google.com/maps/documentation/geocoding/intro

api_key = False    # Setting the api_key as False to proceed with the dummy url provided
# api_key = "Google's API key"    # We can enter the geojson key from the below link if registered
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42    # Setting the key value for the dummy url
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'    # dummy url

else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
    
address = input('Enter location: ')    # Getting the name of the university to get the place_id
parms = dict()    # End parameters of the encoded url
parms['address'] = address    # Adding the location received as the address

if api_key is not False: parms['key'] = api_key    # Adding the dummy key value as the parameter
url = serviceurl + urllib.parse.urlencode(parms)    # Encoding the url
print("Retrieving",url)

url_data = urllib.request.urlopen(url, context=ctx).read().decode()    # Reading and decoding the json data from the url
print('Retrieved', len(url_data), 'characters')

try:    # Try and except block to keep the program running even there is some error in retreiving the json file
    js = json.loads(url_data)    # Loading the json file as python byte element
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':    # If the retrieving is unsuccessful
    print('***Failed To Retrieve***')
    print(url_data)
    
place_id = js['results'][0]['place_id']    # In the js dict, using the key 'results' to go into the reults list
# From the results list going into the first element which is again a dictionary with all data
# Using the key 'place_id' to get the output
print("Place ID of the entered University is :", place_id)