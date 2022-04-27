from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl
import pandas as pd
import os

context =ssl._create_unverified_context()
headers ={'User-Agent': 'Mozilla/5.0'}

url='https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako'
request = Request(url, headers=headers)
response = urlopen(request, context=context)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
result = soup.find_all('div', {'class', 'SbNwzf eeoZZ'})

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
    data.to_csv('data/titles1.csv', encoding='utf-8')