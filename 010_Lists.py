# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.

#Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fname = input("Enter file name: ")    # Reading the file name from user

if len(fname) < 1:    # If no name is entered taking a default file name
    fname = "mbox-short.txt"

fh = open(fname)    # Reading the file in a handle
lines_list = fh.read().splitlines()    # Reading the file line by line and storing it in a list
count = 0    # Variable to count the number of line matching the requirement

for line in lines_list:    # Iterating over each word of the line
    
    if line.startswith('From '):    # Check the condition
        print(line.split()[1])    # Printing the secod element (second word) of the list
        count += 1    # Increasing the count

print("There were", count, "lines in the file with From as the first word")