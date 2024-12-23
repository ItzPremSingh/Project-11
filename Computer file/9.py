# Write a program in python to calculate following series.
# 1+2+3+5+7+11+13+17+...+n

n = int(input("Enter the value of n: "))
sum = 1

if n >= 2:
    sum += 2

for i in range(3, n + 1):
    isPrime = True

    for j in range(2, i // 2 + 1):
        if i % j == 0:
            isPrime = False

    if isPrime:
        sum += i

print("The sum of series is", sum)


# Output

# Enter the value of n: 10
# The sum of series is 55
