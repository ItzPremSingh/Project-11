# Write a program in python to print all prime numbers in between 1 to 1000
# with using for and while loop.

print("Prime numbers using for loop:")
for num in range(1, 1001):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print()

print("Prime numbers using while loop:")
num = 1
while num <= 1000:
    if num > 1:
        i = 2
        while i <= int(num**0.5):
            if num % i == 0:
                break
            i += 1
        else:
            print(num, end=" ")
    num += 1
print()


# Output

# Prime numbers using for loop:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 ......
# Prime numbers using while loop:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 ......
