'''class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 130
        self.travelled_distance = 500

    def __str__(self):
        return (f"Registration Number: {self.registration_number}\n"
                f"Maximum Speed: {self.max_speed} km/h\n"
                f"Current Speed: {self.current_speed} km/h\n"
                f"Travelled Distance: {self.travelled_distance} km")

car = Car("GMO-549", 140)
print(car)'''

'''class Car:
    def __init__(self, registration_number, max_speed):

        self.registration_number = registration_number
        self.max_speed = max_speed

        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):

        self.current_speed += speed_change


        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def print_details(self):

        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.max_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled Distance: {self.travelled_distance} km")

car = Car("GMO-549", 140)
car.accelerate(30)
car.print_details()
car.accelerate(70)
car.print_details()
car.accelerate(50)
car.print_details()
car.accelerate(-200)
car.print_details()'''

'''class Car:
    def __init__(self, registration_number, max_speed):

        self.registration_number = registration_number
        self.max_speed = max_speed

        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):

        self.current_speed += speed_change

        if self.current_speed < 0:
            self.current_speed = 0

        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):

        self.travelled_distance += self.current_speed * hours

    def print_details(self):

        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.max_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled Distance: {self.travelled_distance} km")

car = Car("GMO-549", 142)
car.accelerate(30)
car.print_details()
car.drive(1.5)
car.print_details()
car.accelerate(70)
car.print_details()
car.drive(2)
car.print_details()
car.accelerate(-200)
car.print_details()'''


'''import random

class Car:
    def __init__(self, registration_number, max_speed):

        self.registration_number = registration_number
        self.max_speed = max_speed

        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):

        self.current_speed += speed_change

        if self.current_speed < 0:
            self.current_speed = 0

        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):

        self.travelled_distance += self.current_speed * hours

    def print_details(self):

        print(f"{self.registration_number:<10} {self.max_speed:<15} {self.current_speed:<15} {self.travelled_distance:<15.1f}")

cars = []
for i in range(1, 11):

    registration_number = f"RAM-{i}"

    max_speed = random.randint(100, 200)

    car = Car(registration_number, max_speed)
    cars.append(car)

race_finished = False
while not race_finished:
    for car in cars:

        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)

        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True
            break

print(f"\n{'Registration':<10} {'Max Speed (km/h)':<15} {'Current Speed (km/h)':<15} {'Travelled Distance (km)':<20}")
print("=" * 60)
for car in cars:
    car.print_details()'''


'''class InsufficientBalanceError(Exception):
   
    pass

class NegativeValueError(Exception):
   
    pass

def get_float_input(prompt):
    
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    try:

        balance = get_float_input("Enter account balance: ")
        withdrawal = get_float_input("Enter withdrawal amount: ")

        if balance < 0 or withdrawal < 0:
            raise NegativeValueError("Balance and withdrawal amount must be non-negative.")

        if withdrawal > balance:
            raise InsufficientBalanceError("Withdrawal amount exceeds the account balance.")


        balance -= withdrawal
        print(f"Withdrawal successful. Remaining balance: ${balance:.2f}")

    except InsufficientBalanceError as e:
        print(f"Error: {e}")
    except NegativeValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()'''

'''def write_notes(filename):

    with open(filename, 'w') as file:
        print("Enter your new notes. Type 'STOP' to end.")
        while True:
            note = input("New Note: ")
            if note.upper() == "STOP":
                break
            file.write(note + "\n")
        print(f"New notes have been written to {filename}.")

def read_notes(filename):

    try:
        with open(filename, 'r') as file:
            notes = file.readlines()
            if notes:
                print(f"\nExisting notes in {filename}:")
                for line in notes:
                    print(line.strip())
            else:
                print(f"No notes found in {filename}.")
    except FileNotFoundError:
        print(f"{filename} does not exist. Please write new notes first.")

def append_notes(filename):

    with open(filename, 'a') as file:
        print("Enter additional notes to append. Type 'STOP' to end.")
        while True:
            note = input("Additional Note: ")
            if note.upper() == "STOP":
                break
            file.write(note + "\n")
        print(f"Additional notes have been appended to {filename}.")

def main():
    filename = "notes.txt"  # File to store notes

    while True:
        print("\nChoose an option:")
        print("1. Write new notes (this will overwrite existing notes)")
        print("2. Read existing notes")
        print("3. Append additional notes")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            write_notes(filename)
        elif choice == '2':
            read_notes(filename)
        elif choice == '3':
            append_notes(filename)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()'''

