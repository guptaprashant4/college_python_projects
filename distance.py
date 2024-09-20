# Name: Prashant Gupta
# Program: distance.py
# Purpose: This program will calculate the distance between two points

# Import math module to calculate square root
import math

# Input of the first set of points
x1, y1 = eval(input("""Enter the first set of points
Example: 2,4
=> """))

# Take second set of points as input
x2, y2 = eval(input("Enter the second set of points \n=> "))

# Calculate difference of x and y points and square them
diff_of_x = (x2-x1) ** 2
diff_of_y = (y2-y1) ** 2

# Calculate the distance between those points
distance = round(math.sqrt(diff_of_x + diff_of_y), 2)

# Output the calculated distance
print("The distance between the points is", distance, "units.")