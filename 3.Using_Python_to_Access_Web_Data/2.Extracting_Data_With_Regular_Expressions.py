import re


name = input("Enter the file name : ")
if len(name) < 1 :
    name = regex_sum_42.txt
fh = open(name)
text = fh.read()
numbers = re.findall('[0-9]+', text)
sum = 0
for number in numbers:
    number = int(number)
    sum = sum + number
print(sum)
