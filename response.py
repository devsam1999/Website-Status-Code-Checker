#This Program will help u to check the existance of bulk urls.
#Author Chittaranjan Kumar (@chitta2019) and Sahil Mishra (@devsam1999)
#Just_for_fun
import requests
url_file = open('web.txt', 'r')#replace your file name with web.txt
url=url_file.read()
newurl= url.splitlines()
for x in newurl:
	print(x)
	response = requests.get(x)
	scode=response.status_code
	if scode == 200:
		print("Website found")
	elif scode == 404:
		print("Website Not found")
	else:
		print("Website found")
