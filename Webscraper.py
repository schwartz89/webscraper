import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.courts.act.gov.au/magistrates/lists?collection=magistrates-court-lawlists&mode=rest-js&f.Hearing+date%7Cd=d%3E09Apr2020%3C04May2020+%3A%3A+Coming+month'
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
list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = [] #blank python data list
    for cell in row.findAll('td'): #then this does the same for the 'td' which is html for 'individual cell'
        list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)
        #print(cell.text)
#print to file (.csv). Using csv module
new_file = open("./CourtList.csv","w")
writer = csv.writer(new_file)
writer.writerows(list_of_rows)







# table data location is : table id="search-results" class="table table-bordered table-striped"

#table = soup.find('tbody', attrs={'class': 'stripe'})
#print table.prettify()

#to do:
#check if this is truncating any data, I'm not convinced it is getting all dates