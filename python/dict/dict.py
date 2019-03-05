import requests
from bs4 import BeautifulSoup

url = 'https://dict.naver.com/dekodict/#/search?query='
word = '아들'

res = requests.get(url+word)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
result = soup.find_all('#searchPage_entry > ul > li:nth-child(1) > ul > li:nth-child(1) > p > span')
print(result)


#searchPage_entry > ul > li:nth-child(1) > ul > li:nth-child(1) > p > span
#searchPage_entry > ul > li:nth-child(1) > ul > li:nth-child(2) > p > span
#searchPage_entry > ul > li:nth-child(1) > ul > li:nth-child(3) > p > span