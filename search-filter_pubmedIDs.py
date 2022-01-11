# TODO: Need to "pip install pymed" and "pip install pandas", PyCharm is a preferred IDE
from pymed import PubMed
import requests
from datetime import date
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path


# INPUT PARAMETERS:
search_term = "tetr"
max_results = 20
filter_terms = ["EMSA", "DNase footprinting"]



out_name = search_term+"_"+str(date.today())+".xlsx"


# TODO: Change email to an active email you have access to
pubmed = PubMed(tool="PubMedSearcher", email="doelsnitz@utexas.edu")

    # api request
results = pubmed.query(search_term, max_results=max_results)

# Generate list of dict records which will hold all article details that could be fetch from PUBMED API
    # The article['pubmed_id'] contains a list separated with a comma - take first pubmedId
articleList = [ article.toDict() for article in results ]
articleIDs = [ article['pubmed_id'].partition('\n')[0] for article in articleList ]


print(str(len(articleIDs))+" articles retrieved from search term: "+str(search_term))

    # counter
c = 0
    # initialize list for storing pubmedIDs
filtered_pIDs = []


for pID in articleIDs:
    url = "https://pubmed.ncbi.nlm.nih.gov/" + str(pID)+ "/"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    link = soup.find(class_ = "full-text-links-list")
    if link is None:
        print("invalid BS4 link encountered")
        continue
    fullAccessURL = str(link.findChild("a")['href'])


    try:
        res = requests.get(fullAccessURL)
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

        # Can add as many extra searches here as we want, saving these articles as strings, and searching through those
        # Can also only output IDs so that artcicle can be read in pubmed. 
        if any(word in str(output) for word in filter_terms):
            filtered_pIDs.append(pID)
            print('appended article '+str(pID))
        else:
            print("filter terms not found in article "+str(c))
        c += 1
    except:
        print("request failed for article "+str(c))
        c += 1

print(str(len(filtered_pIDs))+" pubmed articles satisfy search/filter terms")

path = Path('./cache')
file_path = path / out_name

pd.DataFrame(filtered_pIDs).to_excel(file_path, header=False, index=False)


#How to extract specific portions of a text file using Python
#https://www.computerhope.com/issues/ch001721.htm
    

