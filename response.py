import requests
url_file = open('web.txt', 'r')#replace your file name with web.txt
url=url_file.read()
newurl= url.splitlines()
for x in newurl:
	print(x)
	response = requests.get(x)
	print(response.status_code)
