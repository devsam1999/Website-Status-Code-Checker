import requests
url_file = open('web.txt', 'r')#replace your file name with web.txt
url=url_file.read()
newurl= url.splitlines()
for x in newurl:
	print(x,endl=" ")
	response = requests.get(x)
	scode=response.status_code
	if scode == 200:
		print("Website found")
	elif scode == 404:
		print("Website Not found")
	else:
		print("Website found")
