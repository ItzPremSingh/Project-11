# Write a program in python to print all prime numbers in between 1 to 1000
# with using for and while loop.

for number in range(2, 1001):
    if number == 2:
        print("2 is a prime number.")
        continue

    midNumber = number // 2 + 1
    isPrime = True

    for divisor in range(2, midNumber):
        if number % divisor == 0:
            isPrime = False
            break

    if isPrime:
        print(number, "is a prime number.")
