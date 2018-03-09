#scraper.py

#http://christopheviau.com/d3list/

import requests,bs4,os,pprint,re

#k = requests.get('http://christopheviau.com/d3list/')
#Very very very slow
#type(k)
#Instead, we can download the page and save it in a local directory. Open it 

with open('christopheviau.com.html') as f:
	main_string = f.read()


#print(main_string)
#pprint.pprint(main_string)

soup = bs4.BeautifulSoup(main_string,'html.parser')

print(soup.title)
print(soup.p)

#pprint.pprint(soup.find_all(re.compile(r'[<li><a href=]',re.DOTALL|re.MULTILINE|re.VERBOSE)))

# final_list = []
# final = soup.find_all('a')
# for link in final:
# 	final_list.append(link.get("href"))

# print(final_list)

#Now lets try to do this with regular expressions







# b = soup.find_all(re.compile(r'[<a href=]',re.DOTALL|re.MULTILINE|re.VERBOSE))
# print(len(b))

# new_list = []
# for i in b:
# 	g = str(i).lstrip('<a href=').rstrip('">\w</a>')
# 	new_list.append(g)

# print(new_list)