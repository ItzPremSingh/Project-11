# Write a program in python to calculate area and volume of
# cuboid, cube, cylinder and cone.


# Cuboid

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))
height = float(input("Enter the height: "))
area = 2 * (length * breadth + breadth * height + height * length)
volume = length * breadth * height
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
area = 6 * (side * side)
volume = side * side * side
print("Area of cube is", area)
print("Volume of cube is", volume)

# Output

# Enter the side: 5
# Area of cube is 150
# Volume of cube is 125


# Cylinder

pi = 3.14

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))
area = 2 * pi * radius * (radius + height)
volume = pi * radius * radius * height
print("Area of cylinder is", area)
print("Volume of cylinder is", volume)

# Output

# Enter the radius: 5
# Enter the height: 10
# Area of cylinder is 62.83
# Volume of cylinder is 314.15


# Cone

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))
slant_height = (radius**2 + height**2) ** 0.5
area = pi * radius * (radius + slant_height)
volume = (pi * radius * radius * height) / 3
print("Area of cone is", area)
print("Volume of cone is", volume)

# Output

# Enter the radius: 5
# Enter the height: 10
# Area of cone is 31.42
# Volume of cone is 16.67
