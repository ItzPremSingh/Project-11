# Write a program in python to print following pattern :-

string = ""
for i in range(4):
    if i % 2 == 0:
        string = "#" + string

    else:
        string = "$" + string

    print(string)


# Output

# #
# $#
# #$#
# $#$#
