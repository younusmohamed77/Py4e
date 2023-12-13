# Following Links in Python
#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
#We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment
#- Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#    - Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#    - Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
#    - Last name in sequence: Anayah
#- Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Stephany.html
#    - Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#    - Hint: The first character of the name of the last page that you will load is: T

# Importing the necessary file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter an URL : ")    # # Getting the url from the user
html = urllib.request.urlopen(url, context = ctx).read()    # Opening(connecting) to the html file
soup = BeautifulSoup(html, "html.parser")    # Parsing the data to a python readable format

process_counter = int(input('Enter the number of times to repeat the process :'))
link_pos = int(input('Enter the position of the link : '))

tags = soup('a')     # Saving all the anchor tags from the file as a list
print("Retreiving :", url)
print(tags[link_pos - 1].contents[0])

while process_counter:
    temp_url = tags[link_pos - 1].get('href', None)
    print("Retreiving :", temp_url)
    temp_html = urllib.request.urlopen(temp_url, context = ctx).read()    # Opening(connecting) to the html file
    temp_soup = BeautifulSoup(temp_html, "html.parser")    # Parsing the data to a python readable format
    print(tags[link_pos - 1].contents[0])
    tags = temp_soup('a')
    
    process_counter -= 1