import requests
import random
from bs4 import BeautifulSoup
import os

token = os.getenv("TELE_TOKEN")
chat_id = "796125625"
# url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text=안녕하세요"
url = f"https://api.hphk.io/telegram/bot{token}/sendMessage?chat_id={chat_id}&text="

sise_url = "https://finance.naver.com/sise/"
sise_html = requests.get(sise_url).text
sise_soup = BeautifulSoup(sise_html, "html.parser")
sise = sise_soup.select_one("#KOSPI_now").text

lotto = str(random.sample(range(1, 46), 6))

res = requests.get(url+sise)
res = requests.get(url+lotto)
print(res)
# print(url)