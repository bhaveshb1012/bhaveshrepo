'''num = 1
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1'''


'''INCH_TO_CM = 2.54
while True:
    inches = float(input("Enter a value in inches (negative to quit): "))
    if inches < 0:
        print("Negative value entered.")
        break
    centimeters = inches * INCH_TO_CM
    print(f"{inches} inches is equal to {centimeters} centimeters.")'''

'''numbers = []
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    try:

        number = float(user_input)
        numbers.append(number)
    except ValueError:

        print("Invalid input. Please enter a valid number.")
if numbers:
    smallest = min(numbers)
    largest = max(numbers)

    print(f"The smallest number entered is: {smallest}")
    print(f"The largest number entered is: {largest}")
else:
    print("No numbers were entered.")'''
'''
import random
secret_number = random.randint(1, 10)
while True:
    user_guess = input("Guess the number (between 1 and 10): ")
    try:

        guess = int(user_guess)

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Correct! You guessed the number.")
            break
    except ValueError:

        print("Please enter a valid number.")'''
'''
correct_username = "Bhavesh Bhadiyadra"
correct_password = "Bhavesh_Bhadiyadra@1"
attempts = 0
max_attempts = 5
while attempts < max_attempts:

    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        attempts += 1
        print("Incorrect username or password.")
        if attempts < max_attempts:
            print(f"Attempts remaining: {max_attempts - attempts}")
if attempts == max_attempts:
    print("Access denied.")'''

'''
import random
def approximate_pi(num_points):
    points_inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            points_inside_circle += 1
    pi_approximation = 4 * (points_inside_circle / num_points)
    return pi_approximation
num_points = int(input("Enter the number of random points to generate: "))
pi_value = approximate_pi(num_points)
print(f"Approximate value of pi after {num_points} points: {pi_value}")'''

