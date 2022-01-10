import requests

# TODO: Need to "pip install pymed" and "pip install pandas", PyCharm is a preferred IDE
from pymed import PubMed
import pandas as pd
from os.path import abspath

headers = {
    'authority': 'pubmed.ncbi.nlm.nih.gov',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://pubmed.ncbi.nlm.nih.gov/?term=tetr+regulator',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'pm-csrf=W6TcaKK0YLmfXO7lwXvU110Dwc5N3oeGJIECOtkWb8kPhOTcMlgBdklHlR1LhRD0; ncbi_sid=05E72E4C179ACE23_1110SID; _ga=GA1.2.1958737310.1635364455; pmc.article.report=; books.article.report=; IDPORG=VW5pdmVyc2l0eSBvZiBUZXhhcyBhdCBBdXN0aW4=; MyNcbiSigninPreferences=O3VuaXZlcnNpdHlfb2ZfdGV4YXNfYXRfYXVzdGluJg%3D%3D; pm-sessionid=fw76p9dhr07hnhic0hvqo589j7cbz56h; _gid=GA1.2.842281748.1637526816; NIHSMSESSION=ChcJ8lTbBeZQ3iPOVIQMHx4Ze0Tgu+eWcf/PLMxUGNnSNb4DdaUMyIQtjlrhnR9HQ6t263ZJCTpmdS0L3hSKfDOJ2dXNVlHUv9QjG9BiSLe+5dNPFUq4QX/uxrxTmfSPlihF8TOjrh98CjQNuOJsfllmyn5TkvIoGz0XRs/cqEWJkqHta+nfCDCtZMZxQG9RcMRugjnbeIR46pmFSaCBqxTNyPBx3SvHCtb1qUOWXtK6sMBSnSOIJHB6gCHNd7tY6aZTYoPxNg5U6wuudwkxWZqYe0hY9k3bYBxtLNIAKzI2Zmwg10Mpb7jAb0zYHpkk873veeUynEwwqG9JqCgt4pMVmWN004aFNWey+lyCwf/2Y/GKaKcLGPLNIsEp2SZu4NzHRrWGx8KZw2he2k2f3F6OotNjgDeFkqgf5g33tH5C7QnIQOP9FE9LsWXymsL+2zshIlqyIcQZysM9t/hEkcIuJsnPmNcOo/YyeqvY5bH1QaDQo+qC8yy+OQqDE2lrCv0VAmEXyPEckyiDNPd4ei0MrcjhT9g3HBE99n0uzTVfX9t1+b1+ZYpDCNzbxKL51WgstJkZu3cV3rtOaNzlVUdRYL5OhyAwNWFeTquSYQpqf+Dfko3j42PsyOX4yylB9ppdwKywMRcZyGU8XRdXQomrRw+gWiIjtsJSd/YQ35VB8yRaYeJqHmsjyHGdvO0yk1BR2zoy2sZQXtvdFqGqBBIpAZH+esAoG9tXLo24ToG1jM2JdpVJ18Huuo9Kwl7nh7iVgOIRZgBPbrqKP+N2G0ixSknqJZqYzTNhA/5/+XcvD66LtJ9bXZ2i+p1UQ9t9ZH7hlEKh1SMed4HdjiB7XtpSbcE/lphgoZnxKu2lfdR6b/GpdVSY+gktU5QXcmadYfPkbvuSjgZSz0hDEy95P1Ohi6ayDA+3ORsA+46TkVReSB2x5k6QvfqXtQPv4aOozPrP10Hx6wsDKGMXFH7qfmTpMf5IN6molTmZrQA6cIwzR/5vhu6cp+7hMaZMXwIgZuotQy2yvpxEBrdtGRasIoUxwN8X9uiuwP6YA5dp8E8h3aRs7/yD6j3zSJqD/78qra20wsdCQSsUoPRBAzGzrNoVc9BF/lI/KbsOUdhmtYvV18F9rwBY4m8O5RrSqXBl1QTIQ1DifThYL72Awn0h3fxcoORWUp7LSCFQiaa5Oqf34YAp72yWZARXUX3kv17TXCT4RASrNWjn6FZJMRJrp8VtcRlsh8K2; ncbi_prevPHID=CE8DAAF819AA1D6100000000003B003A; WebCubbyUser=IN4VAY2M97S1N6TR5NT475J0PR7JLCZU%3Blogged-in%3Dtrue%3Bmy-name%3Dlgs972%2540eid.utexas.edu%3Bpersistent%3Dtrue%4005E72E4C179ACE23_1110SID; WebEnv=16K1_x%4005E72E4C179ACE23_1110SID; pm-sid=Meed6c9ySHAzVHroXkDmsw:02a77223cb55e9c6aa72e7a4a0a6912f; pm-adjnav-sid=_UgCk_Nnp9LyLOakaXCzvw:02a77223cb55e9c6aa72e7a4a0a6912f; _gat_ncbiSg=1; _gat_dap=1; ncbi_pinger=N4IgDgTgpgbg+mAFgSwCYgFwgEwBFsBCADCQIwDCAogCwCC5AHEQKwkkDM1B7p2D2nIqQB0IgLZxmIADQgArgDsANgHsAhqgVQAHgBdMobJnByARmKjpZ7Y2DMWrIascQqLMkFKwfsRY3kI2Chp6JlY2Tm5efkERcUkfUlt7Sww7c1TXCwwAOQB5HMofIyx0h2EFAGNTZAqlMQrkRGEAcxUYHwBOY1Jqaj9rPyxOkg8eHr6BkHYSkCYk6xssXQg5KDHnZdX16wZjMe6sUlIGfo8zo4EiI1lqJZAiYR5Rc835ZXVNHX1brwePZj3UidGyyZhvABsIwBEOM7D2YIA7MZmFJZBCkkdoejYaU1C0oHAYMgoAB3EAAXwpQA==',
} 


# TODO: Change email to an active email you have access to
pubmed = PubMed(tool="PubMedSearcher", email="email@email.com")

# Change the search term and amount of results desired as needed
search_term = "tetR"
results = pubmed.query(search_term, max_results=300)
articleList = []
articleInfo = []
articleID = []
filteredIDs = []

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
    results = requests.get(url)
    data = results.text
    #print(data)
    if "EMSA" in str(data):
        print(pID)




#response = requests.get('https://pubmed.ncbi.nlm.nih.gov/', headers=headers)

#PMCID = "PMC7324645"

#url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id="+str(pubmed_ID)
#url = "https://pubmed.ncbi.nlm.nih.gov/" + str(pubmed_ID) + "/"
#url = "https://www.ncbi.nlm.nih.gov/pmc/articles/" + str(PMCID) + "/"

#url = "https://www-ncbi-nlm-nih-gov.ezproxy.lib.utexas.edu/pubmed?otool=txutalib"

#url = "https://enterprise.login.utexas.edu/idp/profile/SAML2/POST/SSO?execution=e1s2"

#url = "https://pubmed-ncbi-nlm-nih-gov.ezproxy.lib.utexas.edu/34713957/"

