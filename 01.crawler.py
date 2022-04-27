from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl
import pandas as pd
import os

context =ssl._create_unverified_context()
headers ={'User-Agent': 'Mozilla/5.0'}

url='https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'
request = Request(url, headers=headers)
response = urlopen(request, context=context)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
result = soup.find_all('div', {'class', 'cluster_text_lede'})

if not os.path.exists('data'):
    os.mkdir('data')

titles = []

data = pd.DataFrame({'title': titles})
data.to_csv('data/titles.csv', encoding='utf-8')

for r in result:
    print(r.text)
    titles.append(r.text)
    print(titles)

    data = pd.DataFrame({'title': titles})
    data.to_csv('data/titles.csv', encoding='utf-8')
