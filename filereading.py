#filereading.py
import os

current_directory = os.getcwd()
#print(current_directory)

current_directory_venv = os.path.join(current_directory,'venv')

#print(current_directory_venv)

#An absolute path, which always begins with the root folder
#A relative path, which is relative to the program’s current working directory


dirname = os.path.dirname(current_directory_venv)
basename = os.path.basename(current_directory_venv)
print(dirname)
print(basename)

#print(os.path.split(current_directory_venv))



#Lets start reading files now

f = open('scraper.py')
g = f.read()
f2 = open('newscraper','w')
f2.write('newscraper.py')
f2.write(g)























#with open() as f: