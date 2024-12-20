# Write a program in python to print following pattern :-

#    1
#   12
#  123
# 1234

for i in range(1, 5):
    print(" " * (4 - i), end="")
    for j in range(1, i + 1):
        print(j, end="")

    print()
