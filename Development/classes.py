# class myclass:
#     x=5

# print(myclass)

# class myclass:
#     x=5
#     y=10
# p1=myclass()
# print(p1.x)
# print(p1.y)

# class person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
    
#     def __str__(self):
#         return f"{self.fname} {self.lname}"

# p1 = person("hari","prasath") 
# print(p1)
# print(p1.fname)
# print(p1.fname , p1.lname)



# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=person("hari",21)

# print(p1.name, p1.age)
# print(p1.name)
# print(p1.age)


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def myfun(self):
#         print("hello my name is "+ self.name)

# p1 = person("hari", 21)
# p1.myfun()


# class person:
#     def __init__(idea,name,age):
#         idea.name=name
#         idea.age=age

#     def myfunc(more):
#         print("hello my name is "+more.name)

# p1=person("hari prasath",21)
# p1.myfunc()


# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname

#     def printname(self):
#         print(self.firstname , self.lastname)

# class student(person):
#     pass

# x=student("hari", "prasath")
# x.printname()


class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

class student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)

x=student("raj","kumar")
x.printname()