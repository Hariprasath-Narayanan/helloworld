# x=["c","e","b","a","d"]
# x.sort()
# print(x)

# x=["c","e","b","a","d"]
# x.sort(reverse=True)
# print(x)

def myfunc(n):
    return abs(n-80)

thislist=[100,50,65,82,23]
thislist.sort(key=myfunc)
print(thislist)
