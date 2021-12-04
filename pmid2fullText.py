from pprint import pprint
import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib



pubmed_ID = "32046731"

url = "https://pubmed.ncbi.nlm.nih.gov/" + str(pubmed_ID)+ "/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
link = soup.find(class_ = "full-text-links-list")
#print(link)
fullAccessURL = str(link.findChild("a")['href'])



#Try with 30341075 and 15944459 and 32046731



url = fullAccessURL
res = requests.get(url)
html_page = res.content
soup3 = BeautifulSoup(html_page, 'html.parser')
text = soup3.find_all(text=True)

output = ''
blacklist = [
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'style', 'footer', 
    # there may be more elements you don't want, such as "style", etc.
]

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)

with open ("cache/"+pubmed_ID+"_cached_fullText.txt", mode="w+") as f:
    f.write(output)
