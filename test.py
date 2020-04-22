# import csv


court_list = ["Barack James Obama", "Roger Ramjet"]
search_terms = "Barack Obama"
matches = []
for name_string in court_list:
    for word in search_terms.split(" "):
        if word not in name_string:
            break
    else:
        matches.append(name_string) # triggers when the for loop doesn't break
print(matches)
#very close to being the thing! only downside is that a spelling error in fore or surname invalidates the search for that name.
#i'm sure that is easily fixable
#or just make sure no spelling errors in input - could be a good options to keep output list small


# import tkinter
# from tkinter.constants import *
# tk = tkinter.Tk()
# frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
# frame.pack(fill=BOTH,expand=1)
# label = tkinter.Label(frame, text="Hello, World")
# label.pack(fill=X, expand=1)
# button = tkinter.Button(frame,text="Exit",command=tk.destroy)
# button.pack(side=BOTTOM)
# tk.mainloop()

# from tkinter.filedialog import askopenfilename
# filename = askopenfilename()
# print(filename)

# # client_list = []
# # with open("./CourtList.csv",'rt') as f:
# #   data = csv.reader(f)
# #   for row in data:
# #         client_list.append(row)
# # print(client_list)
#
# new_file = open("./Clients.csv", "w", newline='')
# writer = csv.writer(new_file)
# writer.writerow(["James"])
# writer.writerow(["Adam"])
# writer.writerow(["frank"])