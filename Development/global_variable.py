x = "awesome"
def myfanc():
    global x
    x = "fantastic"
    print("python is " + x )

myfanc()
print("python is " + x)
