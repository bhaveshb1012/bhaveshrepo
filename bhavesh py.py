'''def greet():
    print("Hello Bhavesh!")
    return
print("A new day starts with a greeting.")
greet()
print("Now we can move to other business.")
'''
'''def greet(times):
    for i in range(times):
        print("Round " + str(i+1) + " of saying hello.")
    return
print("A new day starts with a greeting.")
greet(5)
print("Let's greet some more")
greet(2)'''

'''def change():
    city = "Vantaa"
    print("At the end of the function: " + city)
    return
city = "Helsinki"
print("At the beginning in the main program: " + city)
change()
print("At the end of the main program: " + city)'''

'''def sum_of_squares(first, second):
    result = first**2 + second**2
    return result
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = sum_of_squares(number1, number2)
print(f"The sum of squares for numbers{number1:.3f} and {number2:.3f} is {result:.3f}.")'''

'''def inventory(items):
    print("You have the following items:")
    for item in items:
        print("- " + item)
    return

backpack = ["Water bottle", "Map", "Compass"]
inventory(backpack)
backpack.append("Swiss Army knife")
inventory(backpack)'''

'''def inventory(items):
    print("You have the following items:")
    for item in items:
        print("- " + item)
    items.clear()
    return

backpack = ["Water bottle", "Map", "Compass"]
inventory(backpack)
backpack.append("Swiss Army knife")
inventory(backpack)'''

'''rounds = int(input("How many Greetings: "))
finished_rounds = 0
while finished_rounds<rounds:
    print("Good Morning")
    finished_rounds = finished_rounds + 1'''

'''username = input("Enter your name: ")
while username != "Stop":
    print("Welcome, " + username)
    username = input("Enter your name: ")'''

'''number = 1
while number<5:
    print(number)
print("All ready.")'''

'''import random
dice1 = dice2 = rolls = 0
while (dice1!=6 and dice2!=6):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls = rolls + 1
print(f"Rolled {rolls:d} times.")'''

'''import random
dice1 = dice2 = rolls = 0
while (dice1!=6 or dice2!=6):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls = rolls + 1
print(f"Rolled {rolls:d} times.")'''

'''import random
rounds = 0
total_rolls = 0

while rounds < 10000:
    dice1 = dice2 = rolls = 0
    while (dice1!=6 or dice2!=6):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        rolls = rolls + 1
    print(f"Rolled {rolls:d} times.")
    rounds = rounds + 1
    total_rolls = total_rolls + rolls
average_rolls = total_rolls/rounds
print(f"Average rolls required: {average_rolls:6.2f}")'''

'''first = 1
while first <= 5:
    second = 1
    while second <= 5:
        print(f"{first} times {second} is {first*second}")
        second = second + 1
    first = first + 1'''

'''command = input("Enter a command: ")
while command!= "stop":
    if command == "MAYDAY":
        break
    print("Execution command: " + command)
    command = input("Enter command: ")
print("Execution stopped.")'''

'''command = input("Enter a command: ")
while command!= "stop":
    if command == "MAYDAY":
        break
    print("Executoin command: " + command)
    command = input("Enter command: ")
else:
    print("Goodbye.")
print("Execution stopped."'''
