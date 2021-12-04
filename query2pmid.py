from pymed import PubMed

# Create a PubMed object that GraphQL can use to query
pubmed = PubMed(tool="MyTool", email="my@email.address")

# Input query here
query = 'tetr regulator'

# Execute query
results = pubmed.query(query, max_results=100)

# For each article that is retrieved from pubmed searches
for article in results:

    # Extract information from the article and save to variables
    article_id = article.pubmed_id
    article_doi = article.doi
    title = article.title
    if article.keywords:
        if None in article.keywords:
            article.keywords.remove(None)
        keywords = '", "'.join(article.keywords)

    # Print and formatinfo about the article
    print("Article DOI" + str(article_doi) + "\n" + "Title: " + title + "\n")
    print(type(article))

    #All pubmed articles are automatically covereted to XML files to be parsed 

