import csv
i = input('Enter file path')

f = open(i,'r')
content = f.read()
print(content)
