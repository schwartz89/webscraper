import requests
from bs4 import BeautifulSoup

url = 'https://www.courts.act.gov.au/magistrates/lists?collection=magistrates-court-lawlists&mode=rest-js&f.Hearing+date%7Cd=d%3E09Apr2020%3C04May2020+%3A%3A+Coming+month'
wholesite = requests.get(url, headers= {'User-Agent': 'Mozilla/5.0'})
html = wholesite.content

#pull the data into beautifulsoup which reads website data better then display it formatted nicely using the prettify function
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())
table = soup.find('table', id="search-results")

print(table.prettify())


# table data location is : table id="search-results" class="table table-bordered table-striped"

#table = soup.find('tbody', attrs={'class': 'stripe'})
#print table.prettify()
