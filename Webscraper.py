# can I install packages from a python script?
from typing import Tuple

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
client_list = 'MANSOUR'

# matches = [i for i in courtlist_data if client_list in i]
matches = [row for row in courtlist_data if client_list in row]
# submatches =

for row in courtlist_data:
    for cell in row:
    #if any([item in client_list for item in row]):
        if client_list in cell: #need to reword this so it says if any x in y, because we are potentially comparing a larger list to a smaller one, as opposed to our previous 'in' functions
            matches.append(row)
           #could add "unless it's already there" to prevent double-up #for some reason this line makes 'matches are : [[]] instead of []

https://stackoverflow.com/questions/6105777/how-to-compare-a-list-of-lists-sets-in-python
# any([x in "foof" for x in ["bar", "foo", "foobar"]])
# set(a).intersection(b)

# needs an extra 'in' iteration? # can I add at the end "or in subdivision of ame" which is to say "is it in the room or is it in the cupboard in the room??
# ^ so this says: look through the courtlist data item (i) by item (rows), if your client list name is in that item, put that item (the row) in this list.
# note it is only working for single string client_list keywords too, not a list. This is because it is comparing the whole list to a whole row, not iterating through the client list
# what you need is a NESTED FOR LOOP (see tab)
print("Matches are : " + str(matches))



# none are working. I think because it is not a list, but rather a list of lists. So it is trying to match the provided string to a whole row, not a cell.
# so i think i need to iterate along the row, not just through. So needs another nested loop like above

# an alternate way of doing this compare would be get both client list and court list in csv form and do a delta compare, keep only matches. Probably no simpler, same issues.


# to do:
# add list-compare functionality to compare list of clients to court lists. csv - csv compare? then display entire row of matched name
# add list-input functionality. Only working with single strings
# add supreme court functionality
# get the script to install its dependencies ?Pip
# get it to output somewhere useful
# find out how to make it run on another pc. USB .exe?, terminal? (see resources)
