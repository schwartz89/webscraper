import csv
# client_list = []
# with open("./CourtList.csv",'rt') as f:
#   data = csv.reader(f)
#   for row in data:
#         client_list.append(row)
# print(client_list)

new_file = open("./Clients.csv", "w", newline='')
writer = csv.writer(new_file)
writer.writerow(["James"])
writer.writerow(["Adam"])
writer.writerow(["frank"])