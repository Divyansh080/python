# wap to input number and display fectorial.

n = int(input("Enter number:"))
facto = 1

for i in range(1,n+1):
    facto *= i
    # facto = facto*i

    print(f"factorial of {n}*{i} is {facto}")
