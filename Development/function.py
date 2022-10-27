# def washing_machine():
#     print("wash")
#     print("spin")
#     print("hot water washing")
#     print("dry")

# print("set1")
# washing_machine()

# print("set2")
# washing_machine()

# print("set3")
# washing_machine()

# print("set4")
# washing_machine()

# def my_function():
#     print("hello world")

# my_function()

# def addition(a,b):
#     print(a+b)

# addition(1,2)

# def multiplication(a,b,c):
#     print(a*b*c)

# multiplication(10,2,2)

# def my_function(fname):
#     print(fname + " prasath")

# my_function("hari")


# def my_function(fname,lname):
#     print(fname+" "+lname)

# my_function("hari","prasath")

# def addition(*add):
#     print()
# for i in addition():
#     print

# a=10
# b=5

# def subraction():
#     print(a-b)

# subraction()
# subraction()
# subraction()

# x=int(input())
# y=int(input())

# def my_function(x,y):
#     print(x+y)

# my_function(x,y)



# def multiplication(*number):
#     product=1
#     for items in number:
#         product=product*items
#     print(product)

# multiplication(2,4,5,6)
# multiplication(10,20)
# multiplication(3,4,5,5,5,5,5,5)


# def multiplication(*numbers):
#     product=1
#     for items in numbers:
#         product=product*items
#     print(product)

# a = tuple(input())
# print(type(a))
# print(a)

# multiplication()


#keywords arguments
# def my_funtion(child1,child2,child3):
#     print("the youngest child is " + child3)

# my_funtion(child1="hari",child2="ashwin",child3="lakshith")


# def my_function(**keys):
#     print("his last name is " +keys['lname'])
#     # for items in keys:
#     #     print(items)
#     #     print("his last name is "+items)
# my_function(fname="hari",lname="prasath")

# def my_function(country="india"):
#     print("i am from "+ country)

# my_function()
# my_function("brazil")
# my_function("norway")

# def my_function(food):
#     for item in food:
#         print(item)

# fruits=["apple","banana","cherry"]

# my_function(fruits)


# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# light=int(input("enter a num1 : "))
# fan=int(input("enter a num2 : "))
# x=add(light,fan)
# y=sub(light,fan)
# z=mul(x,y)

# print(z)

# def my_function():
#     pass


#recursion

def tri_recursion(k):
    if k>0:
        result=k + tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result
print("\n\nRecursion example result")
tri_recursion(6)

