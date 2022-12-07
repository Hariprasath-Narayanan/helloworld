# name = "jhon smith"
# age = 20
# patient_new = True

# name = (input("Enter your name : "))
# print("good morning"+" "+ name)

# name = input("what is your name ?")
# color = input("what is your fav color?")
# print(name + " like " + color)


# birth_year = int(input("Enter your birth year: "))
# age = 2022 - birth_year
# print(age)

# user_height_cm = int(input("Enter your height in cm: "))
# user_height_feet = user_height_cm / 30
# print(user_height_feet)

# course = "python's course for beginners"
# print(course)

# interview = '''hai hari
# how are you 
# how was your interview
# how long your day 
# '''
# print(interview)

# course = "python was fun"

# print(course[0:6])

# first_name = "Hari"
# last_name = "prasath"

# msg = f"{first_name} [{last_name}] is a coder"

# print(msg)


# course = "python is  fun"
# print(course.upper())


# course = "python is  fun"
# print(course.replace("fun","gooooooood"))

# print("python" in course)

# hot = False
# if hot:
#     print("it is a hot day")
#     print("drink plenty of water")
# else:
#     print("it is a cold day")
#     print("wear warm clothes")
# print("Enjoy your day")

# house_price = 100000

# has_good_credit = False 

# if has_good_credit:
#     down_payment = 0.1 * house_price
# else:
#     down_payment = 0.2 * house_price
# print(f"down payment : {down_payment}")


# high_income = False
# high_credit = False

# if high_income or high_credit:
#     print("you eligible for loan")
# else:
#     print("you not eligible for loan")

#ex---1

# temperature = int(input("what is temperature now? "))

# if temperature >= 30:
#     print("it's a hot day")
# elif temperature <=10:
#     print("it's a cold day")

# else:
#     print("it's neither hot or cold")


# ex--2

# user_name = str(input("Enter your name here: "))

# if len(user_name) < 3:
#     print("name must be at least 3 characters")
# elif len(user_name) > 50:
#     print("name must be a maximum of 50 characters")
# else:
#     print("name looks good")


#weight converter program

# user_weight = int(input("Enter your weight: "))
# unit = input("(L)bs  or (k)g: ")
# if unit.upper() == "L":
#     converted = user_weight * 0.45
#     print(f"you are  {converted} kilos")
# else :
#     converted = user_weight / 0.45
#     print(f"you are {converted} pounds")


# while loop

# i = 1
# while i <= 5 :
#     print(i)
#     i = i + 1
# print("Done")

# secret_num = 6
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit :
#     guess = int(input("guess: "))
#     guess_count += 1
#     if guess == secret_num:
#         print("your guess is correct")
#         break
# else:
#     print("your guess is worng")

# # car game

# command = ""
# while command!="quit":
#     command = input("> ").lower
#     if command == "start":
#         print("car started..")
#     elif command == "stop":
#         print("car stopped.")
#     elif command == "help":
#         print("""
#         start - to start car
#         stop - to stop car
#         quit - to quit car
#         """)
#     elif command == "quit":
#         break
# else:
#     print("sorry i don't understand")   


# price = [10,20,30]
# total = 0
# for i in price:
#     total += i
# print(f"total = {total}")

# nested loop

# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")

# number = [5,2,5,2,2]
# for items in number:
#     output = ""
#     for count in range(items):
#         output += "x"
#     print(output) 

# list = [20,25,50,35,80]
# max = list[0]
# for i in list:
#     if i > max:
#         max = i
# print(max)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# matrix[0][2] = 30
# print(matrix[0][2])

# matrix = [
#      [1,2,3],
#      [4,5,6],
#      [7,8,9]
# ]
# for row in matrix:
#     print(row)


