# Write a program in python to calculate area and volume of
# cuboid, cube, cylinder and cone.

import math

print("1. Cuboid")
print("2. Cube")
print("3. Cylinder")
print("4. Cone")
choice = int(input("Enter your choice: "))

if choice == 1:
    length = float(input("Enter the length: "))
    breadth = float(input("Enter the breadth: "))
    height = float(input("Enter the height: "))
    area = 2 * (length * breadth + breadth * height + height * length)
    volume = length * breadth * height
    print("Area of cuboid is", area)
    print("Volume of cuboid is", volume)

elif choice == 2:
    side = float(input("Enter the side: "))
    area = 6 * (side * side)
    volume = side * side * side
    print("Area of cube is", area)
    print("Volume of cube is", volume)

elif choice == 3:
    radius = float(input("Enter the radius: "))
    height = float(input("Enter the height: "))
    area = 2 * math.pi * radius * (radius + height)
    volume = math.pi * radius * radius * height
    print("Area of cylinder is", area)
    print("Volume of cylinder is", volume)

elif choice == 4:
    radius = float(input("Enter the radius: "))
    height = float(input("Enter the height: "))
    area = math.pi * radius * (radius + math.sqrt(radius * radius + height * height))
    volume = (math.pi * radius * radius * height) / 3
    print("Area of cone is", area)
    print("Volume of cone is", volume)

else:
    print("Invalid choice")
