# Write a program in python to check week days from week number.

number = int(input("Enter the week number (1-7): "))

if number == 1:
    day = "Monday"

elif number == 2:
    day = "Tuesday"

elif number == 3:
    day = "Wednesday"

elif number == 4:
    day = "Thursday"

elif number == 5:
    day = "Friday"

elif number == 6:
    day = "Saturday"

elif number == 7:
    day = "Sunday"

else:
    day = "Invalid week number"

print(day)
