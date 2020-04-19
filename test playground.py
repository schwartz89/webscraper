x = "harry"
print("x is: " + str(x))
print("x is this type: " + str(type(x)))

# if isinstance(x, list):
#     print("it's a list of this many names: ")
#     for i in x:
#         print('*')
# if isinstance(x, tuple):
#     print("it's a tuple of this many names: ")
#     for i in x:
#         print('*')
# if isinstance(x, str):
#     print("it's probably a single string of this many names")
#     print('*')
# ^ this works but is fragile and overoptimised

#maybe:
if isinstance(x,str):
    x = [x]
print("it doesn't matter what datatype it is now. It is this many names:")
for i in x:
    print('*')

# x = [x]
# print("x is: " + str(x))

# x = []
# x.append("barry")
# print("x is: " + str(x))

#print("x is: " + str(x))
#x.append(name)

# print("x is: " + str(x))
# print("x is this type: " + str(type(x)))
# print("there are this many names in the list: ")
#
#
# if x is str:
#     print('*')
#
# if x is list:
#     for i in x:
#         print('*')
#
# if x is tuple:
#     print('wtf is a tuple')
#
# #none of these are correctly identifying cclass

