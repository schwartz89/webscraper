# can I install packages from a python script?

import requests
from bs4 import BeautifulSoup
import csv

# to extend table length add ?num_ranks=9999
url = 'https://www.courts.act.gov.au/magistrates/lists?num_ranks=9999'
wholesite = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = wholesite.content

# pull the data into beautifulsoup which reads website data better then display it formatted nicely using the prettify function
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', id="search-results")

# what does this do?
# it iterates through every occasion of the word 'tr' (which is html for 'row' and on each occasion of 'tr' it runs an operation:
# this operation is to loop through all the 'td' (html for 'individual cell') within the row and prints the text only.
# so in short this section grabs every individual cell and prints the writing within, cutting out all the html code, while keeping the order of the data.
# these must be beautifulsoup functions because they seem to intuit that tr is a row, not a single piece of data
# think of this loop function like running your finger along reading text in a book. You iterate down line by line, but across each word (cell) in the line.
courtlist_data = []
for row in table.findAll('tr'):
    list_of_cells = []  # blank python data list
    for cell in row.findAll('td'):  # then this does the same for the 'td' which is html for 'individual cell'
        list_of_cells.append(cell.text)
    courtlist_data.append(list_of_cells)
    # print(cell.text)
# print to file (.csv). Using csv module
new_file = open("./CourtList.csv", "w", newline='')
writer = csv.writer(new_file)
writer.writerow(["Case Number", "Name", "Hearing Date"])  # manually inserting headings instead of looping through thead
writer.writerows(courtlist_data)

# CHAPTER II: the nae finder
# this builds a list of matches by iterating through the web text list and putting the item into the new list when it CONTAINS the keyword.
# the item put in the list is the entire row. At present this function doesn't know how to search in each cell and so can't match partial keywords yet
print("The original list is : " + str(courtlist_data))
client_list = 'JERMAINE'

# matches = [i for i in courtlist_data if client_list in i]
matches = [row for row in courtlist_data if client_list in row]
# submatches =
for row in courtlist_data:
    for cell in row:
        if client_list in cell:
            print(row)  # change this last line to 'add to matches'

# needs an extra 'in' iteration? # can I add at the end "or in subdivision of ame" which is to say "is it in the room or is it in the cupboard in the room??
# ^ so this says: look through the courtlist data item (i) by item (rows), if your client list name is in that item, put that item (the row) in this list.
# note it is only working for single string client_list keywords too, not a list. This is because it is comparing the whole list to a whole row, not iterating through the client list
# what you need is a NESTED FOR LOOP (see tab)
print("Matches are : " + str(matches))

# ctrl q is doc

# NESTED FOR LOOP
# for i in range(1,6):
#         for j in range(i):
#             print("*",end=' ')
#         print()

# ["foo" in a for a in ["fo", "o", "foobar"]]
# [False, False, True]
# Caveat. Lists are iterables, and the in method acts on iterables, not just strings

# none are working. I think because it is not a list, but rather a list of lists. So it is trying to match the provided string to a whole row, not a cell.
# so i think i need to iterate along the row, not just through. So needs another nested loop like above

# experiment
# for hay in haystack:
#   if needle in hay:
#     return hay


# to do:
# add list-compare functionality to compare list of clients to court lists. csv - csv compare? then display entire row of matched name
# add supreme court functionality
# get the script to install its dependencies
# get it to output somewhere useful
