print("Thank you for choosing Python Pizza Deliveries!")
size = input("Size of Your pizza type: \nS for Small,\nM for Medium,\nL for Large\n")
add_pepperoni = input("Want pepperoni Y or N\n")
extra_cheese = input("Add extra cheese Y or N\n")

bill_for_small = int(15)
bill_for_medium = int(20)
bill_for_large = int(25)

pepperoni_for_small = int(2)
pepperoni_for_medium_large = int(3)
extra_cheese_for_small_medium_large = int(1)

if size == "S" and add_pepperoni == "Y" and extra_cheese == "Y":
    print(f"Your final bill is: ${bill_for_small + pepperoni_for_small + extra_cheese_for_small_medium_large}.")
elif size == "S" and add_pepperoni == "Y" and extra_cheese == "N":
    print(f"Your final bill is: ${bill_for_small + pepperoni_for_small}.")
elif size == "S" and add_pepperoni == "N" and extra_cheese == "Y":
    print(f"Your final bill is: ${bill_for_small + extra_cheese_for_small_medium_large}.")
elif size == "S" and add_pepperoni == "N" and extra_cheese == "N":
    print(f"Your final bill is: ${bill_for_small}.")

if size == "M" and add_pepperoni == "Y" and extra_cheese == "Y":
    print(f"Your final bill is: ${bill_for_medium + pepperoni_for_medium_large + extra_cheese_for_small_medium_large}.")
if size == "M" and add_pepperoni == "Y" and extra_cheese == "N":
    print(f"Your final bill is: ${bill_for_medium + pepperoni_for_medium_large}.")
if size == "M" and add_pepperoni == "N" and extra_cheese == "Y":
    print(f"Your final bill is: ${bill_for_medium + extra_cheese_for_small_medium_large}.")
if size == "M" and add_pepperoni == "N" and extra_cheese == "N":
    print(f"Your final bill is: ${bill_for_medium}.")

if size == "L" and add_pepperoni == "Y" and extra_cheese == "Y":
    print(f"Your final bill is: ${bill_for_large + pepperoni_for_medium_large + extra_cheese_for_small_medium_large}.")
if size == "L" and add_pepperoni == "Y" and extra_cheese == "N":
    print(f"Your final bill is: ${bill_for_large + pepperoni_for_medium_large}.")
if size == "L" and add_pepperoni == "N" and extra_cheese == "Y":
    print(f"Your final bill is: ${bill_for_large + extra_cheese_for_small_medium_large}.")
if size == "L" and add_pepperoni == "N" and extra_cheese == "N":
    print(f"Your final bill is: ${bill_for_large}.")
else:
    "Invalid Input"
