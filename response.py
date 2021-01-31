import requests
url_file = open('web.txt', 'r')
url=url_file.read()
newurl= url.splitlines()
#print (newurl)
for x in newurl:
	print(x)
	response = requests.get(x)
	print(response.status_code)
