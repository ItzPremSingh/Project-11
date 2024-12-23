# Write a program in python to check entered year is leap year.

year = int(input("Enter year: "))

if year % 4 == 0:
    print(year, "is a leap year.")

else:
    print(year, "is not a leap year.")


# Output

# Enter year: 2000
# 2000 is a leap year
