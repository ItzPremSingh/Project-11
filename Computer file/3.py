# Write a program in python to print a series of Mersenne number up to n.
# With using for and while loop.

# --- for loop ---

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    print((2**i) - 1, end=", ")

print()


# --- while loop ---

n = int(input("Enter the value of n: "))
i = 1

while i <= n:
    print((2**i) - 1, end=", ")
    i += 1

print()


# Output

# Enter the value of n: 10
# 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023
