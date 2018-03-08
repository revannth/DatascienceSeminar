#phonenumber.py


#Importing the library to import the objects of the re module
import re

test_string = "MY PHONE NUMBER IS 123-456-789"

Pattern = re.compile(r"\d\d\d-\d\d\d-\d\d\d")

Matchme = Pattern.search(test_string)


print("Phone number found:"+Matchme.group())