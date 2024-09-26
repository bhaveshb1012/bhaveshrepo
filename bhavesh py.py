'''
import random
def roll_dice():
    """Returns a random dice roll between 1 and 6."""
    return random.randint(1, 6)

def main():
    """Rolls the dice until a 6 is rolled and prints each result."""
    result = 0
    while result != 6:
        result = roll_dice()
        print(f"Rolled: {result}")

if __name__ == "__main__":
    main()'''
'''
import random
def roll_dice(sides):
    return random.randint(1, sides)
def main():
    sides = int(input("Enter the number of sides on the dice: "))
    result = 0
    while result != sides:
        result = roll_dice(sides)
        print(f"Rolled: {result}")
if __name__ == "__main__":
    main()'''

'''
def gallons_to_liters(gallons):
    liters_per_gallon = 3.78541
    return gallons * liters_per_gallon
def main():
    while True:
        try:
            gallons = float(input("Enter the volume in gallons (negative to quit): "))
            if gallons < 0:
                print("So Sorry, Can't find Value")
                break
            liters = gallons_to_liters(gallons)
            print(f"{gallons} gallons is equal to {liters:.2f} liters.")
        except ValueError:
            print("Please enter a valid number.")
if __name__ == "__main__":
    main()'''

'''
def sum_of_list(numbers):
    return sum(numbers)
def main():
    test_list = [1, 2, 3, 4, 5,6,7,8,9,10]
    total = sum_of_list(test_list)
    print(f"The sum of {test_list} is {total}.")
if __name__ == "__main__":
    main()'''

'''
def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_list = remove_odd_numbers(original_list)
    print(f"Original list: {original_list}")
    print(f"Filtered list (only even numbers): {filtered_list}")
if __name__ == "__main__":
    main()'''
'''
import math
def calculate_unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)  # Area in square centimeters
    area_in_square_meters = area / 1_000_000  # Convert area to square meters
    unit_price = price / area_in_square_meters  # Price per square meter
    return unit_price
def main():
    diameter1 = float(input("Enter the diameter of the first pizza in cm: "))
    price1 = float(input("Enter the price of the first pizza in euros: "))
    diameter2 = float(input("Enter the diameter of the second pizza in cm: "))
    price2 = float(input("Enter the price of the second pizza in euros: "))
    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)
    print(f"Unit price of the first pizza: €{unit_price1:.2f} per square meter")
    print(f"Unit price of the second pizza: €{unit_price2:.2f} per square meter")

    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas offer the same value for money.")
if __name__ == "__main__":
    main()'''


