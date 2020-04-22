# TODO find out how to make it run on another pc. USB .exe? (see resources x 2)
# TODO make script work for two word name inputs? # either by forcing input client list to seperate surname, or by having matching function loop through words within a string.


#package imports
import requests
from bs4 import BeautifulSoup
import csv

### CHAPTER I: Getting the website data

## scooping the data from the website using requests package
# TIP: to extend table length we add ?num_ranks=9999
MC_url = 'https://www.courts.act.gov.au/magistrates/lists?num_ranks=9999'
MC_wholesite = requests.get(MC_url, headers={'User-Agent': 'Mozilla/5.0'})
MC_html = MC_wholesite.content

SC_url = 'https://www.courts.act.gov.au/supreme/lists?num_ranks=9999'
SC_wholesite = requests.get(SC_url, headers={'User-Agent': 'Mozilla/5.0'})
SC_html = SC_wholesite.content

## pull the data into beautifulsoup which reads website data better then display it formatted nicely using the prettify function
MC_soup = BeautifulSoup(MC_html, 'html.parser')
MC_table = MC_soup.find('table', id="search-results")
SC_soup = BeautifulSoup(SC_html, 'html.parser')
SC_table = SC_soup.find('table', id="search-results")

## Get the text from the table
# this iterates through the table rows then cells (tr means table row in html, td means individual cell)
# think of this loop function like running your finger along reading text in a book. You iterate down line by line, but across each word (cell) in the line.

courtlist_data = []
#MC
for row in MC_table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text)
    courtlist_data.append(list_of_cells)
#SC
for row in SC_table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text)
    courtlist_data.append(list_of_cells)

## print to .csv using csv module
# #redundant
#new_file = open("./CourtList.csv", "w", newline='')
#writer = csv.writer(new_file)
#writer.writerow(["Case Number", "Name", "Hearing Date"])  # manually inserting headings instead of looping through 'thead' in the html
#writer.writerows(courtlist_data)

### CHAPTER II: the name finder
## builds a list of matches
# by iterating through the web text list and putting the item into a list of matches when it contains the client name.

#input or import client names
client_list = 'kristy' #[['harry','mcguckin'],['james','gary']]



## open from csv file
# file_loc = "./Clients.csv"
# with open(file_loc, 'rt') as f:
#   data = csv.reader(f)
#   for row in data:
#         client_list.append(row)

#TODO have it read from csv # ?should I turn this whole thing into a function so you can input client list name into terminal?

matches = []


# converts any solo string to list so all input we get will be a list, easier to iterate through
if isinstance(client_list, str):
     client_list = [client_list]

#extend vs append. Append adds it as a sublist extend tacks it onto the list

#flattens list od lists into normal lists
def flatten(input):
  output_list = []
  for item in input:
    if isinstance(item, list):
      output_list.extend(flatten(item))
    else: output_list.append(item)
  return output_list


client_list = flatten(client_list)


def listcompare(client_name, courtdata):
    for row in courtdata:
        for cell in row:
            if client_name.casefold() in cell.casefold():
                matches.append(row)


# runs individual names through our listcompare function
for name in client_list:
        listcompare(name, courtlist_data)



print("You searched for the names: " + str(client_list))
print("The court list is : " + str(courtlist_data))
print("The matches are : " + str(matches))

#Write match results to csv
#todo put cap on file size eg: if len(matches): break print('error too many matches')
new_file = open("./Matches.csv", "w", newline='')
writer = csv.writer(new_file)
writer.writerow(["You searched for the names: " + str(client_list)])
writer.writerow(["The matches are:"])
writer.writerow(["Case Number", "Name", "Hearing Date"])
writer.writerows(matches)

#TODO optional. Add user GUI to select client list file like this:
# from tkinter.filedialog import askopenfilename
# filename = askopenfilename()

