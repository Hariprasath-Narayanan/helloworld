def simple_interest(p,n,r):
    return(p*n*r/100)

x = int(input("Enter p = "))
y = int(input("Enter n = "))
z = int(input("Enter r = "))
si = simple_interest(x,y,z)
print(si)