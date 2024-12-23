# Write a program in python to print following pattern :-

number = 65

for i in range(1, 4):
    for j in range(1, i + 1):
        print(chr(number), end="")
        number += 1

    print()

for i in range(2, 0, -1):
    for j in range(1, i + 1):
        print(chr(number), end="")
        number += 1

    print()


# Output


# A
# BC
# DEF
# GH
# I
