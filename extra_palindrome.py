# User Defined Function to check if a number is a palindrome
unit--3
def palindrome(num):
    rev = 0
    original = num
    while num != 0:
        temp = num % 10
        rev = (rev * 10) + temp
        num = num // 10  
    if original == rev:
        print("Number is palindrome.")
    else:
        print("Number is not palindrome.")

    return rev

num = int(input("Enter a number:"))
p = palindrome(num)
