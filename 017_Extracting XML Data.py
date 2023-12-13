# Extracting Data from XML

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1936336.xml (Sum ends with 10)

# Importing the necessary modules

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the url : ")    # Reading the URL from the user
xml = urllib.request.urlopen(url, context = ctx).read()    # Reading the XML file in that URL

stuff = ET.fromstring(xml)    # Getting the 'TREE STRUCTURE' of the XML file

counts = stuff.findall('.//count')    # Making a list of all count elements from the tree

counts_sum = 0

for count in counts:
    counts_sum += int(count.text)    # count.text gives the element 'count' at 0x0XXXXX
    
print("Sum of counts :",counts_sum)