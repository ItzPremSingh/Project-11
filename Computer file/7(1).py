# Write a program in python to print following pattern :-

# #
# $#
# #$#
# $#$#

index = 1
char = ("$", "#")
string = ""

for i in range(1, 5):
    string = char[index % 2] + string
    index += 1
    print(string)
