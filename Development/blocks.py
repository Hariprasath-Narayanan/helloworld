# for i in range(1,14):
#     print("no. {} squared is {} and cubed is {}" .format(i, i**2, i**3))
#     print("=" * 80)

name = input("enter your name: ")
age = int(input("how old are you, {0}? ".format(name)))
print(age)

if age>=18:
    print("yor are enough to vote")

else:
    print("please come back in {} years".format(18-age))
    