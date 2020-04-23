# TODO find out how to make it run on another pc. USB .exe? (see resources x 2)
# TODO pyinstaller not finding required packages so exe not working
# I assume becuase my cmd and powershell terminals can't find requests or bs4 either - so they must be installed
# in a place they can't see. This happens when i install stuff from the pycharm terminal. This must be instanced
# so I either need to point pyinstaller to the instance location where the packages live. Or install them all in
# my pc terminal. Not sure if this is bad practice though

#package imports
import requests
from bs4 import BeautifulSoup
import csv
from tkinter.filedialog import askopenfilename

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

### CHAPTER II: the name finder
## builds a list of matches
# by iterating through the web text list and putting the item into a list of matches when it contains the client name.

#input or import client names
client_list = []
# open from csv file
file_loc = askopenfilename(title='Select client names list', filetypes=(('csv files','*.csv'),('all files','*.*'))) #"./Clients.csv"
with open(file_loc, 'rt') as f:
  data = csv.reader(f)
  for row in data:
        client_list.append(row)
#todo (optional) add dialog box where you can either A. select file from pc B. input name manually
# could also add info box here about type of input accepted

## tidying up the input
# converts any solo string to list so all input we get will be a list, easier to iterate through
if isinstance(client_list, str):
     client_list = [client_list]

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
            for word in client_name.split(" "): #chops the search term name into individual words
                if word.casefold() not in cell.casefold():
                    break
            else:
                matches.append(row) # triggers when the for loop doesn't break

# runs individual names through our listcompare function
matches = []
for name in client_list:
        listcompare(name, courtlist_data)

### Chapter III: Output
print("You searched for the names: " + str(client_list))
print("The court list is : " + str(courtlist_data))
print("The matches are : " + str(matches))

#Write match results to csv
new_file = open("./Matches.csv", "w", newline='')
writer = csv.writer(new_file)
if len(matches) > 10000:
    print('Too many matches, will not export this to file')
else:
    writer.writerow(["You searched for the names: " + str(client_list)])
    writer.writerow(["The matches are:"])
    writer.writerow(["Case Number", "Name", "Hearing Date"])
    writer.writerows(matches)

#todo (optional) add popup saying results printed to csv here. click to open
# todo (optional) print match results deliniated by search term ie: Kristy matched with:, James matched with: useful for searching a whole client list at once

