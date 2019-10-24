from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

number = [] 
c = []
html = urlopen('http://pi.noauth.fail/').read()
html = html.decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
all_href = soup.find_all('a')
for l in all_href:
    number.append(l['href'])

print("Raspberry Pi web site total:%d" % len(number))
for i in range(len(number)):
    country = number[i].split('.')[-1]
    if country == 'de' or 'Germany' in country:
        c.append(country)

print("Germany:%d" % len(c))

