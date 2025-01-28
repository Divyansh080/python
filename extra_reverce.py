# User Defined Function to reverse a number

def reverse_number(num):
    new_num = 0
    while num > 0:
        digit = num % 10
        new_num = new_num * 10 + digit
        num = num // 10
    return new_num


num = int(input("Enter a number: "))
new_num = reverse_number(num)

print(f"The reverse of {num} is {new_num}")
