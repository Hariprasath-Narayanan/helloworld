# fruits = ["apple","banana","cherry","kiwi","mango"]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)

# fruits = ["apple","banana","cherry","kiwi","mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# fruits = ["apple","banana","cherry","kiwi","mango"]
# newlist =[x for x in fruits if x != "apple"]
# print(newlist)

# newlist = [i for i in range(10)]
# for i in newlist:
#     print(i)

fruits = ["apple","banana","cherry","kiwi","mango"]
newlist= [i.upper() for i in fruits ]
print(newlist)
