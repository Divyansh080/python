p = float(input("enter the amount:"))
r = float(input("enter the rate of interest:"))
y = int(input("enter the year:"))

ci = p *(1 +  r  /100)** y - p  
print(ci)
