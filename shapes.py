"""
******************************
CS 1026 - Assignment 1 – Shapes and Sizes
Code by: Muniver Kaur Kharod
File created: September 23, 2024
******************************
This file is used to calculate the area and perimeter of various 2-dimensional
shapes (Rectangle,triangle,circle,trapezoid and hexagon). It must ask the user for
input values based on the shape selected and output the final calculated values.
"""
#use the import math module to extend list of mathematical functions (ie using PI)
import math

#Greet the user and indicate what the calculator does
print("Hello, welcome to the area and perimeter calculator!")

#Prompt the user to enter any of the listed 2D shapes
shape_name = input("Please enter a 2D shape (Rectangle, Triangle, Circle, Trapezoid, Hexagon): ").strip().lower()

#Use function to validate if entered value is positive
def validate_positive(value):
    #check if the value entered is less than or equal to zero
    if value <= 0:
        print("Invalid value entered.")
        return False
    return True

#Check and process the input if 'rectangle' is selected
if shape_name == 'rectangle':
    #Tell user to enter the width and height values
    width_value = float(input("Enter the width: "))
    height_value = float(input("Enter the height: "))

    #Validate the height and width values and proceed if both values are positive
    if validate_positive(width_value) and validate_positive(height_value):

        #Function to calculate the perimeter of the rectangle
        def calculate_perimeter():
            perimeter = 2 * width_value + 2 * height_value
            print(f"Perimeter: {perimeter:.2f}")

        #Function to calculate the area of the rectangle
        def calculate_area():
            area = width_value * height_value
            print(f"Area: {area:.2f}")

        #Utilize the functions to calculate the perimeter and area
        calculate_perimeter()
        calculate_area()

#Check and process the input if 'triangle' is selected
elif shape_name == 'triangle':

    #Tell user to enter the base, two sides, and height values
    base_value = float(input("Enter the base value(b): "))
    side_two = float(input("Enter the value for side 2(a): "))
    side_three = float(input("Enter the value for side 3(c): "))
    height_value = float(input("Enter the height(h): "))

    # Validate all values and proceed if the values are positive
    if all(validate_positive(v) for v in [base_value, side_two, side_three, height_value]):

        #Function to calculate the perimeter of the triangle
        def calculate_perimeter():
            perimeter = base_value + side_two + side_three
            print(f"Perimeter: {perimeter:.2f}")

        #Function to calculate the area of the triangle
        def calculate_area():
            area = (base_value * height_value) / 2
            print(f"Area: {area:.2f}")

        #Utilize the functions to calculate the perimeter and area
        calculate_perimeter()
        calculate_area()

#Check and process the input if 'circle' is selected
elif shape_name == 'circle':

    #Prompt user to enter the circle's radius
    radius_value = float(input("Enter the radius: "))

    #Validate the radius value
    if validate_positive(radius_value):

        #Function to calculate the perimeter of the circle
        def calculate_perimeter():
            perimeter = 2 * radius_value * math.pi
            print(f"Perimeter: {perimeter:.2f}")

        #Function to calculate the area of the circle
        def calculate_area():
            area = math.pi * radius_value ** 2
            print(f"Area: {area:.2f}")

        #Utilize the functions to calculate the perimeter and area
        calculate_perimeter()
        calculate_area()

#Check and process the input if 'trapezoid' is selected
elif shape_name == 'trapezoid':
    #Tell user to enter the top, bottom, two sides, and height values from the user
    top_value = float(input("Enter the value for the top(t): "))
    bottom_value = float(input("Enter the value for the bottom(b): "))
    left_side = float(input("Enter the value for the left side(l): "))
    right_side = float(input("Enter the value for the right side(r): "))
    height_value = float(input("Enter the height(h): "))

    # Validate all values and proceed if the values are positive
    if all(validate_positive(v) for v in [top_value, bottom_value, left_side, right_side, height_value]):

        #Function to calculate the perimeter of the trapezoid
        def calculate_perimeter():
            perimeter = top_value + bottom_value + left_side + right_side
            print(f"Perimeter: {perimeter:.2f}")

        #Function to calculate the area of the trapezoid
        def calculate_area():
            area = ((top_value + bottom_value) / 2) * height_value
            print(f"Area: {area:.2f}")

        #Utilize the functions to calculate the perimeter and area
        calculate_perimeter()
        calculate_area()

#Check and process the input if 'hexagon' is selected
elif shape_name == 'hexagon':
    side_value = float(input("Enter the value for the side: "))

    # Validate all values and proceed if the values are positive
    if validate_positive(side_value):
        #Function to calculate the perimeter of the hexagon
        def calculate_perimeter():
            perimeter = 6 * side_value
            print(f"Perimeter: {perimeter:.2f}")

        #Function to calculate the area of the hexagon
        def calculate_area():
            area = (3 * math.sqrt(3) / 2) * side_value ** 2
            print(f"Area: {area:.2f}")

        #Utilize the functions to calculate the perimeter and area
        calculate_perimeter()
        calculate_area()

#Handle the invalid shape inputs
else:
    print("Invalid shape entered.")

#end
