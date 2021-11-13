import requests

pubmed_ID = "4304705"

url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id="+str(pubmed_ID)

#url = "https://www-ncbi-nlm-nih-gov.ezproxy.lib.utexas.edu/pubmed?otool=txutalib"

#url = "https://enterprise.login.utexas.edu/idp/profile/SAML2/POST/SSO?execution=e1s2"

#url = "https://pubmed-ncbi-nlm-nih-gov.ezproxy.lib.utexas.edu/34713957/"

results = requests.get(url)

data = results.text

print(data)

