# unit 2.3

s1 = int(input("Enter marks:"))
s2 = int(input("Enter marks:"))
s3 = int(input("Enter marks:"))
s4 = int(input("Enter marks:"))

total = s1+s2+s3+s4
pr = total/4

print(f"Total: {total}")
print(f"Percentage: {pr}") # formated string.

if s1>=40 and s2>=40 and s3>=40 and s3>=40 :
    print("Result :  Pass")
    if pr>=70 :
        print("grade : A")
    elif pr >=60 and pr<70:
        print("grade : B")
    elif pr <=50 and pr<60 :
        print("grade : C")
    elif pr <=40 and pr<50 :
        print("grade : D")
else :
    print("Result: Fail")
