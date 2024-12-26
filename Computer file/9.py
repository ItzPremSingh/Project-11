# Write a program in python to calculate following series.
# 1+2+3+5+7+11+13+17+...+n

n = int(input("Enter the value of n: "))
sum = 1

for i in range(2, n + 1):
    isPrime = True

    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            isPrime = False
            break

    if isPrime:
        sum += i

print("The sum of series is", sum)


# Output

# Enter the value of n: 10
# The sum of series is 55
