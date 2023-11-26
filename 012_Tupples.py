# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file name: ")    # Reading the file name from user

if len(name) < 1:    # If no name is entered taking a default file name
    name = "mbox-short.txt"

handle = open(name)    # Reading the file in a handle
lines_list = handle.read().splitlines()    # Reading the file line by line and storing it in a list
hours_dict = {}

for line in lines_list:    # Iterating over each word of the line
    
    if line.startswith('From '):    # Check the condition for received mail
        time = line.split()[5][0:2]    # Getting the time in hours from the line
        
        if time in hours_dict:    # If the hour va;ue is already in the dict increasing the value by 1
            hours_dict[time] += 1
            
        else:
            hours_dict[time] = 1    # If not creating a key value pair with count as 1
            
sorted_dict = dict(sorted(hours_dict.items()))    # Sorting the items of the dictionary

for time in sorted_dict:    # Looping over the dictionary to print the desired output
    print(time, sorted_dict[time])
    