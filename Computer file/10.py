# Write a program in python to calculate area and volume of
# cuboid, cube, cylinder and cone.


# Cuboid

l = float(input("Enter the length: "))
b = float(input("Enter the breadth: "))
h = float(input("Enter the height: "))
area = 2 * (l * b + b * h + h * l)
volume = l * b * h
print("Area of cuboid is", area)
print("Volume of cuboid is", volume)

# Output

# Enter the length: 10
# Enter the breadth: 5
# Enter the height: 2
# Area of cuboid is 100
# Volume of cuboid is 10


# Cube

side = float(input("Enter the side: "))
area = 6 * (side**2)
volume = side**3
print("Area of cube is", area)
print("Volume of cube is", volume)

# Output

# Enter the side: 5
# Area of cube is 150
# Volume of cube is 125


# Cylinder

pi = 3.14

r = float(input("Enter the radius: "))
h = float(input("Enter the height: "))
area = 2 * pi * r * (r + h)
volume = pi * r**2 * h
print("Area of cylinder is", area)
print("Volume of cylinder is", volume)

# Output

# Enter the radius: 5
# Enter the height: 10
# Area of cylinder is 62.83
# Volume of cylinder is 314.15


# Cone

r = float(input("Enter the radius: "))
h = float(input("Enter the height: "))
l = (r**2 + h**2) ** 0.5
area = pi * r * (r + l)
volume = (pi * r**2 * h) / 3
print("Area of cone is", area)
print("Volume of cone is", volume)

# Output

# Enter the radius: 5
# Enter the height: 10
# Area of cone is 31.42
# Volume of cone is 16.67
