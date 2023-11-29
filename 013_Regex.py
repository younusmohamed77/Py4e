import re

def sum_of_numbers(file_name):
    fh = open(file_name)
    num_list = []
    num_sum = 0

    for line in fh:
        temp_list = re.findall('[0-9]+',line.rstrip())
    
        if len(temp_list) > 0:
            num_list.append(temp_list)
    for i in num_list:
        for j in i:
            num_sum += int(j)
        
    return num_sum

sample = input("Enter the smaple file name:")
actual = input("Enter the actual file name:")
print("The sum of all numbers in the sample file is :",sum_of_numbers(sample))
print("The sum of all numbers in the sample file is :",sum_of_numbers(actual))