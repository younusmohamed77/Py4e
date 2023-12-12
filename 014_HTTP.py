#Exploring the HyperText Transport Protocol
#You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.
#http://data.pr4e.org/intro-short.txt

import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = 'https://data.pr4e.org/intro-short.txt'
my_socket.connect((url, 80))
![image.png](attachment:image.png)
![image.png](attachment:image.png)
![image.png](attachment:image.png)
![image.png](attachment:image.png)