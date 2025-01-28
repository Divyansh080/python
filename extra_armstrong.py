def armstrong(num):
    og=num
    rev=0
    while num!=0:
        temp=num%10
        rev=rev+(temp**3)
        num=num/10
    if(og==rev):
        print("number is armstrong.")
    else:
        print("number is not armstrong.")
    return rev
num=int(input("Enter a number:"))
a=armstrong(num)
