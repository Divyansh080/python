'''
15.Write a program to print factorial number using function.
'''


def fecto():
    n = int(input("Enter the number: "))
    fect = 1
    for i in range(1,n+1):
        fect = fect*i
    print(f"factorial of {n} is: {fect}")

print(fecto())
    
