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


# Cube

side = float(input("Enter the side: "))
area = 6 * (side * side)
volume = side * side * side
print("Area of cube is", area)
print("Volume of cube is", volume)


# Cylinder
pi = 3.14

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))
area = 2 * pi * radius * (radius + height)
volume = pi * radius * radius * height
print("Area of cylinder is", area)
print("Volume of cylinder is", volume)


# Cone

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))
slant = (radius**2 + height**2) ** 0.5
area = pi * radius * (radius + slant)
volume = (pi * radius * radius * height) / 3
print("Area of cone is", area)
print("Volume of cone is", volume)
