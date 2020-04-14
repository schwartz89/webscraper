#can I install packages from a python script?

import requests
from bs4 import BeautifulSoup
import csv

#to extend table length add ?num_ranks=9999
url = 'https://www.courts.act.gov.au/magistrates/lists?num_ranks=9999'
wholesite = requests.get(url, headers= {'User-Agent': 'Mozilla/5.0'})
html = wholesite.content

#pull the data into beautifulsoup which reads website data better then display it formatted nicely using the prettify function
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', id="search-results")

#what does this do?
#it iterates through every occasion of the word 'tr' (which is html for 'row' and on each occasion of 'tr' it runs an operation:
#this operation is to loop through all the 'td' (html for 'individual cell') within the row and prints the text only.
#so in short this section grabs every individual cell and prints the writing within, cutting out all the html code, while keeping the order of the data.
# these must be beautifulsoup functions because they seem to intuit that tr is a row, not a single piece of data
# think of this loop function like running your finger along reading text in a book. You iterate down line by line, but across each word (cell) in the line.
list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = [] #blank python data list
    for cell in row.findAll('td'): #then this does the same for the 'td' which is html for 'individual cell'
        list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)
        #print(cell.text)
#print to file (.csv). Using csv module
new_file = open("./CourtList.csv","w",newline='')
writer = csv.writer(new_file)
writer.writerow(["Case Number", "Name", "Hearing Date"]) # manually inserting headings instead of looping through thead
writer.writerows(list_of_rows)


#CHAPTER II: the nae finder

print("The original list is : " + str(list_of_rows))
client_list = 'ADAM NEWMAN'
matches = [i for i in list_of_rows if client_list in i]
print("Matches are : " + str(matches))

#none are working. I think because it is not a list, but rather a list of lists. So it is trying to match the provided string to a whole row, not a cell.
#so i think i need to iterate along the row, not just through. So needs another nested loop like above

# experiment
# for hay in haystack:
#   if needle in hay:
#     return hay



# to do:
# add list-compare functionality to compare list of clients to court lists. csv - csv compare? then display entire row of matched name
# add supreme court functionality
# get the script to install its dependencies