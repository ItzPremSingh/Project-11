# Write a program in python to print following pattern :-

number = 1
times = 2

for i in range(1, 4):
    for j in range(1, i + 1):
        print(number, end=" ")

        number *= times
        times += 1

    print()


# Output

# 1
# 2 6
# 24 120 720
