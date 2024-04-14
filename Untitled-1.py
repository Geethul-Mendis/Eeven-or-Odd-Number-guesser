def check_number(n):
    if n % 2 != 0:
        print("Odd")
    elif n >= 2 and n <= 5:
        print("Even")
    elif n >= 6 and n <= 20:
        print("Odd")
    else:
        print("Even")

# Input
num = int(input("Enter a positive integer: "))

# Check the number
check_number(num)
