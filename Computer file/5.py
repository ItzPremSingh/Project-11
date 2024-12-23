# Write a program in python to check entered number is prime number or not.
# With using for and while loop.

# --- for loop ---

number = int(input("Enter the number: "))

if number == 2:
    isPrime = True

elif number <= 1:
    isPrime = False

for i in range(2, number // 2 + 1):
    isPrime = True
    if number % i == 0:
        isPrime = False

if isPrime:
    print(number, "is a prime number.")

else:
    print(number, "is not a prime number.")


# --- while loop ---

number = int(input("Enter the number: "))

if number == 2:
    isPrime = True

elif number <= 1:
    isPrime = False

i = 2
while i <= number // 2:
    isPrime = True
    if number % i == 0:
        isPrime = False

    i += 1

if isPrime:
    print(number, "is a prime number.")

else:
    print(number, "is not a prime number.")


# Output

# Enter the number: 5
# 5 is a prime number.
