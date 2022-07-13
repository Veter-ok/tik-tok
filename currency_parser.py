# pip3 install beautifulsoup4
# pip3 install requests
import requests
from bs4 import BeautifulSoup

URL = 'https://www.x-rates.com/table/?from=RUB&amount=1'
r = requests.get(URL)

soup = BeautifulSoup(r.content, "html.parser")
rateList = soup.findAll("table", {"class": "ratesTable"})[0].findAll("tbody")

for tableVal in rateList:
	trList = tableVal.findAll("tr")
	for trVal in trList:
		currency = trVal.findAll("td")[0].text
		value = trVal.findAll("td")[2].text
		print(f"{currency} - {value}₽")