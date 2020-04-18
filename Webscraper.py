# TODO can I install dependencies from a python script? ?PIP

#package imports
import requests
from bs4 import BeautifulSoup
import csv

### CHAPTER I: Getting the website data

## scooping the data from the website using requests package
# TIP: to extend table length we add ?num_ranks=9999
url = 'https://www.courts.act.gov.au/magistrates/lists?num_ranks=9999'
wholesite = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = wholesite.content

## pull the data into beautifulsoup which reads website data better then display it formatted nicely using the prettify function
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', id="search-results")

## Get the text from the table
# this iterates through the table rows then cells (tr means table row in html, td means individual cell)
# think of this loop function like running your finger along reading text in a book. You iterate down line by line, but across each word (cell) in the line.
courtlist_data = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text)
    courtlist_data.append(list_of_cells)

## print to .csv using csv module
new_file = open("./CourtList.csv", "w", newline='')
writer = csv.writer(new_file)
writer.writerow(["Case Number", "Name", "Hearing Date"])  # manually inserting headings instead of looping through 'thead' in the html
writer.writerows(courtlist_data)

### CHAPTER II: the name finder
## builds a list of matches
# by iterating through the web text list and putting the item into a list of matches when it contains the client name.

client_list = 'Stewart', 'SUPPRESSED', 'Van' #TODO have it read from csv # ?should I turn this whole thing into a function so you can input client list name into terminal?

matches = []

def listcompare(client_name, courtdata):
    for row in courtdata:
        for cell in row:
            if client_name.casefold() in cell.casefold():
                matches.append(row)

for name in client_list:
    listcompare(name, courtlist_data)

print("The original list is : " + str(courtlist_data))
print("Matches are : " + str(matches))

# TODO add supreme court functionality (scoop data from supreme court url then append it on to the dataset)
# TODO get it to output somewhere useful (terminal? csv?)
# TODO find out how to make it run on another pc. USB .exe? (see resources)
# TODO merge this branch into master and go back to master