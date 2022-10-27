# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year" :1964
# }
# print(thisdict["brand"])

# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year" :1964,
#     "year":2020
# }
# print(thisdict)

# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year" :1964
# }
# print(len(thisdict))

# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year" :1964
# }
# x=thisdict["model"]
# print(x)


# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year" :1964
# }
# x=thisdict.get("model")
# print(x)

# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year" :1964
# }
# x=thisdict.keys()
# print(x)

# car={
#     "brand":"ford",
#     "model":"mustang",
#     "year" :1964
# }
# x=car.keys()
# print(x)
# car["color"]="white"
# print(x)


# car={
#     "brand":"ford",
#     "model":"mustang",
#     "year" :1964
# }
# x=car.values()
# print(x)


# thisdict={
#     "name":"hari",
#     "age":21,
#     "class":"python"
# }
# x=thisdict.keys()
# print(x)


# thisdict={
#     "name":"hari",
#     "age":21,
#     "class":"python"
# }
# x=thisdict.values()
# print(x)


# thisdict={
#     "name":"hari",
#     "age":21,
#     "class":"python"
# }
# x=thisdict.values()
# print(x)
# thisdict["year"]=2001
# print(thisdict)
# thisdict["class"]="mech"
# print(thisdict)


# thisdict={
#     "name":"hari",
#     "age":21,
#     "class":"python"
# }
# x=thisdict.items()
# print(x)


# thisdict={
#     "name":"hari",
#     "age":21,
#     "class":"python"
# }
# if "class" in thisdict:
#     print("yes")


# thisdict={
#     "name":"hari",
#     "age":21,
#     "class":"python"
# }
# thisdict.update({"class":"mech"})
# print(thisdict)


thisdict={
    "name":"hari",
    "age":21,
    "class":"python"
}
thisdict.pop("class")
print(thisdict)
