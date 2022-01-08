# TODO: Need to "pip install pymed" and "pip install pandas", PyCharm is a preferred IDE
from pymed import PubMed
import pandas as pd
from os.path import abspath

# TODO: Change email to an active email you have access to
pubmed = PubMed(tool="PubMedSearcher", email="email@email.com")

# Change the search term and amount of results desired as needed
search_term = "tetr regulator"
results = pubmed.query(search_term, max_results=50)
articleList = []
articleInfo = []
articleID = []

for article in results:
    articleDict = article.toDict()
    articleList.append(articleDict)

# Generate list of dict records which will hold all article details that could be fetch from PUBMED API
for article in articleList:
    # The article['pubmed_id'] contains a list separated with a comma - take first pubmedId
    pubmedId = article['pubmed_id'].partition('\n')[0]
    articleID.append(pubmedId)


#print(articleID)


from pprint import pprint
import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib
import xml.etree.ElementTree as ET



for pID in articleID:
    url = "https://pubmed.ncbi.nlm.nih.gov/" + str(pID)+ "/"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    link = soup.find(class_ = "full-text-links-list")
    if link is None:
        continue
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

    #print(output)
    #Can add as many extra searches here as we want, saving these articles as strings, and searching through those
    #Can also only output IDs so that artcicle can be read in pubmed. 
    if "EMSA" in str(output): 
        f = open("readme.txt" + str(pID), "a+")
        f.write("________STARTING NEXT ARTICLE HERE_____")
        f.write(output)


#How to extract specific portions of a text file using Python
#https://www.computerhope.com/issues/ch001721.htm
    



    
