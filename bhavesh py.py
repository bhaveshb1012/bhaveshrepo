print("Hello Bhavesh")

name = input("Name? ")
print(f"Hello, {name}! Nice to meet you!")

import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"The area of the circle with radius {radius} is {area:.2f}")

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = 2 * (length + width)
area = length * width
print(f"The perimeter of the rectangle is {perimeter:.2f}")
print(f"The area of the rectangle is {area:.2f}")

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

sum_of_numbers = num1 + num2 + num3
product_of_numbers = num1 * num2 * num3
average_of_numbers = sum_of_numbers / 3

print(f"The sum of the numbers is: {sum_of_numbers}")
print(f"The product of the numbers is: {product_of_numbers}")
print(f"The average of the numbers is: {average_of_numbers:.2f}")

LOT_TO_GRAMS = 13.3
POUND_TO_LOTS = 32
TALENT_TO_POUNDS = 20

talents = int(input("Enter the number of talents: "))
pounds = int(input("Enter the number of pounds: "))
lots = int(input("Enter the number of lots: "))

total_lots = (talents * TALENT_TO_POUNDS * POUND_TO_LOTS) + (pounds * POUND_TO_LOTS) + lots
total_grams = total_lots * LOT_TO_GRAMS

kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print(f"The total weight is {kilograms} kilograms and {grams:.2f} grams.")
