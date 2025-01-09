# 3.2 wap to print prime number.

n = int(input("Enter a number: "))

# Loop through all numbers from 2 to n
for num in range(2, n+1):
    is_prime = True  # Assume the number is prime
    
    for i in range(2, num):
        if num % i == 0:  # If divisible by any number other than 1 and itself
            is_prime = False
            break
    
    if is_prime:
        print(num)  
