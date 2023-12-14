# Extracting Data from JSON
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below: We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1936337.json (Sum ends with 32)

# Importing the necesarry files and methods

import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignoring SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the url :")    # Getting the url from user
json_data = urllib.request.urlopen(url, context = ctx).read().decode()    # Reading the json file from url and decoding it
js = json.loads(json_data)    # Loading the element of json into a dictionary of strings
count_sum = 0    # Variable to hold the sum

for comment in js['comments']:    # Considering comments as a key in js dict, iteration over the value of comments which is a list
    count_sum += comment['count']
    
print("The sum of all counts is :",count_sum)