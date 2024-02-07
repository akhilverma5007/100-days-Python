#Randomisation and Python Lists
import random
random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
random_float * 5
print(random_float)

"""
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
Important, the first letter should be capitalised and spelt exactly like in the example e.g. "Heads", not "heads".
There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, 
either 0 or 1. Then use that number to print out "Heads" or "Tails".
e.g. 1 means Heads 0 means Tails
"""

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

# Lists
listOfFriuits = ["Apple", "Orange", "Banana"]
print(listOfFriuits)
print(listOfFriuits[0])
print(listOfFriuits[-2])
listOfFriuits.append("New Fruit") # to add the item to end of the list
listOfFriuits.extend(["a","b","c"]) # add a new list
print(listOfFriuits)

listOfRollNos = [1,2,3,4,5,6,7,8]
print(listOfRollNos)


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]
map = [line1, line2, line3]
position = input()
print(f"{line1}\n{line2}{line3}")
