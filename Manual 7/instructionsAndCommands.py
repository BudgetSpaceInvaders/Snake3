# length = float(input("Please type the length of your rectangle: "))
# height = float(input("Please type the height of your rectangle: "))
# print(f"The perimeter of your rectangle is {2*(length+height)} centimeters. \n "
#       f"The area of your rectangle is {length*height} square centimeters.")


width, height = map(float, input("Enter width and height (separated by space): ").split())
print(f"Area: {width*height:.2f}, Perimeter: {2*(width+height):.2f}")
