
#csv.py

import csv

# f = open('cleaned_data.csv')
# k = csv.reader(f)

# for i in k:
# 	print(i)



import json


json_data = '{"name":"Revannth","class":"MTech"}'

k = json.loads(json_data)
print(k)

original = json.dumps(k)
print(original)