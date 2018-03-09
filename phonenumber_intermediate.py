#phonenumber_intermediate.py

#phonenumber.py


#Importing the library to import the objects of the re module
import re

test_string = "MY PHONE NUMBER IS 040-12345678"

Pattern = re.compile(r"(\d\d\d)-(\d\d\d\d\d\d\d\d)")

Matchme = Pattern.search(test_string)

areacode,mainnum = Matchme.groups()
print("Area code:"+areacode)
print("Main Number:"+mainnum)