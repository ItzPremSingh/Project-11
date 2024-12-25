# Write a program in python to check entered number is prime number or not.
# With using for and while loop.

number = int(input("Enter a number to check if it is prime: "))

print("Checking using for loop:")
if number > 1:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


print("Checking using while loop:")
if number > 1:
    i = 2
    while i <= int(number**0.5):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            break
        i += 1
    else:
        print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


# Output

# Enter a number to check if it is prime: 7
# Checking using for loop:
# 7 is a prime number.
# Checking using while loop:
# 7 is a prime number.
