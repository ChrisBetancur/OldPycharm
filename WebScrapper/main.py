import os
import requests
from bs4 import BeautifulSoup

url = "https://lichess.org/"
reponse = requests.get(url)

'''if reponse.ok:
	print("Hello")
	soup = BeautifulSoup(reponse.text, "lxml")
	title = str(soup.find("title"))
	print(soup)

	title = title.replace("<title>", "")
	title = title.replace("</title>", "")
	print("The title is : " + str(title))

os.system("pause")'''

# URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find(id="blind-mode"))

# print(soup.prettify())

var = 767

print(var // 10)
print((var//10)//10)


