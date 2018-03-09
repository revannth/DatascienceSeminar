
#csv.py

# import csv

# f = open('cleaned_data.csv')
# k = csv.reader(f)

# for i in k:
#  	print(i)



import json

json_data = '{"name":"Revannth","class":"MTech"}'
print(type(json_data))
k = json.loads(json_data)
print(type(k))
print(k)
original = json.dumps(k)
print(original)