# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file name: ")    # Reading the file name from user

if len(name) < 1:    # If no name is entered taking a default file name
    name = "mbox-short.txt"

handle = open(name)    # Reading the file in a handle
lines_list = handle.read().splitlines()    # Reading the file line by line and storing it in a list
sender_dict = {}

for line in lines_list:    # Iterating over each word of the line
    
    if line.startswith('From '):    # Check the condition for received mail
        sender = line.split()[1]    # Getting the sender name from the line
        
        if sender in sender_dict:    # If the sender is already in the dict increasing the value by 1
            sender_dict[sender] += 1
            
        else:
            sender_dict[sender] = 1    # If not creating a key value pair with count as 1
            
max_count = 0    # Variable to hold the maximum value

for sender in sender_dict:    # Looping over the dictionary to find the maximum count
    
    if max_count < sender_dict[sender]:    # If block to check the maximum and assign the respective values to print
        max_count = sender_dict[sender]
        max_mailer = sender

print(max_mailer, max_count)