# Write a program in python to print a series of Mersenne number up to n.
# With using for and while loop.

n = int(input("Enter a number to print Mersenne numbers up to: "))


print("Mersenne numbers using for loop:")
for i in range(1, n + 1):
    mersenne = (2**i) - 1
    if mersenne <= n:
        print(mersenne, end=" ")
    else:
        break
print()


print("Mersenne numbers using while loop:")
i = 1
while True:
    mersenne = (2**i) - 1
    if mersenne <= n:
        print(mersenne, end=" ")
        i += 1
    else:
        break
print()


# Output

# Enter a number to print Mersenne numbers up to: 10
# Mersenne numbers using for loop:
# 1 3 7
# Mersenne numbers using while loop:
# 1 3 7
