# Write a program in python to check topper
# first, second, third, pass and fail position in result.

marks = int(input("Enter the marks: "))

if marks >= 80:
    print("First position")

elif marks >= 60:
    print("Second position")

elif marks >= 40:
    print("Third position")

elif marks >= 33:
    print("Pass")

else:
    print("Fail")


# Output

# Enter the marks: 80
# First position
