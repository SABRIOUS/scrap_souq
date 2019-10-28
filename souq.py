from bs4 import BeautifulSoup
import requests

data = requests.get("https://egypt.souq.com/eg-ar/samsung/s/?as=1&section=2&page=1").text

soup = BeautifulSoup(data,'html.parser')

all_price = soup.find_all('h3',{'class':'itemPrice'})
new_price = []
for price in all_price:
    new_price.append(price.string.split()[0])

print(new_price)
