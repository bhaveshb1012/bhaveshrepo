list3 = []

names = input("Enter your name: ")
while names != "Exit":
    list3.append(names)  # Add the name to the list
    names = input("Enter names (or type 'Exit' to finish): ")
print("Your list of names:", list3)
n = input("Do you want to remove an element from the list? (Y or N): ")
if n == 'Y' or n == 'y':
    element_to_remove = input("Enter the name you want to remove: ")
    if element_to_remove in list3:
        list3.remove(element_to_remove)
        print(f"{element_to_remove} has been removed.")
    else:
        print(f"{element_to_remove} is not in the list.")

print("Updated list of names:", list3)
