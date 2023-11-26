# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

# X-DSPAM-Confidence:    0.8475

# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname).readlines()
spam_con_list = []

for line in fh:

    if line.startswith("X-DSPAM-Confidence:"):
        pos_0 = line.find('0')
        line_spam_con = float(line[pos_0:pos_0+6])
        spam_con_list.append(line_spam_con)
        
total_con = 0

for i in spam_con_list:
    total_con += i
    
print("Average spam confidence:",total_con/len(spam_con_list))