# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.

# You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")    # Reading the file name from user
fh = open(fname)    # Opening the file in file handle
lines_list = fh.read().splitlines()    # Reading line by line as per the problem
words_list = []    # List to hold the unique values

for line in lines_list:    # Iterating line by line

    for word in line.split():    # Iterating over each line

        if word not in words_list:    # Checking if the word is already present 
            words_list.append(word)    # Addding the word to the list if not already present

words_list.sort()    # Sorting the list using sort() function
print(words_list)x`