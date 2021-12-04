# TODO: Need to "pip install pymed" and "pip install pandas", PyCharm is a preferred IDE
from pymed import PubMed
import pandas as pd
from os.path import abspath

# TODO: Change email to an active email you have access to
pubmed = PubMed(tool="PubMedSearcher", email="email@email.com")

# Change the search term and amount of results desired as needed
search_term = "transcription"
results = pubmed.query(search_term, max_results=5000)
articleList = []
articleInfo = []

for article in results:
    articleDict = article.toDict()
    articleList.append(articleDict)

# Generate list of dict records which will hold all article details that could be fetch from PUBMED API
for article in articleList:
    # The article['pubmed_id'] contains a list separated with a comma - take first pubmedId
    pubmedId = article['pubmed_id'].partition('\n')[0]
    # Append article info to dictionary
    if (article['methods'] != None):
        articleInfo.append({u'pubmed_id':pubmedId,
                           u'Title':article['title'],
                           u'Keywords':article['keywords'],
                           u'Journal':article['journal'],
                           u'Abstract':article['abstract'],
                           u'Conclusions':article['conclusions'],
                           u'Methods':article['methods'],
                           u'Results': article['results'],
                           u'Copyrights':article['copyrights'],
                           u'Doi':article['doi'],
                           u'PublicationDate':article['publication_date'],
                           u'Authors':article['authors']})

# Generate Pandas DataFrame from list of dictionaries
articlesPD = pd.DataFrame.from_dict(articleInfo)

# TODO: Name the xml file to be descriptive of the the data being requested and change 'userHere' appropriately
# Convert data to XML file
#export_csv = articlesPD.to_xml(r'C:/Users/lakshmis/Desktop/Dataresults.xml', index=None)
#export_csv = articlesPD.to_csv (r'C:/Users/lakshmis/Desktop/export_dataframe.csv', index = None, header=True)
#export_csv = articlesPD.to_csv('testfile.csv')
export_xml = articlesPD.to_xml('testfile12345.xml')

print("Executed query and finished exporting results for " + f'"{search_term}"')


# If resuts = None
# Use pubmed API queries
# same search
# turn it into xml
# parse through


# Look for ways to login through my credentials
#use PubMed API to return Xml and form dictionat with sections of code

# When I login, acess that URL!!!! 
