#For Loops, Ramge and Code Blocks

fruits = ["apple", "banana", "orange", "chiku"]
for each in fruits:
    print(each)
    # print(each + "Pie")

print(len(fruits))

#Problem 1
"""
You are going to write a program that calculates the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
The average height can be calculated by adding all the heights together and dividing by the total number of heights.
"""

print("Welcome! Calculation of Average Student Height from a list of heights")
student_heights = input().split()  #.split method splits a string into a list
print(student_heights)
print(len(student_heights))

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

totalHeight = 0
for height in student_heights:
    totalHeight += height    
print(f"total height = {totalHeight}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(totalHeight / number_of_students)
print(f"average height = {average_height}")

#Problem 2
"""
You are going to write a program that calculates the highest score from a List of scores.
e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
Important you are not allowed to use the max or min functions. The output words must match the example. i.e
The highest score in the class is: x
"""

print("Write scores to calculate highest amongst them. ")
listOfScores = input().split()
print(listOfScores)

for n in range(0, len(listOfScores)):
    listOfScores[n] = int(listOfScores[n])

maxScore = 0
for each in listOfScores:
    if(each > maxScore):
        maxScore = each

print(f"The highest score in the class is: {maxScore}")

#Print total of 1 to 100 numbers
total = 0
for number in range(1, 101):
    print(number)
    total += number
print(total)

#For loop with Range
for num in range(1, 11):
    print(num)

#Steps by 3
for num in range(1, 11, 3): 
    print(num)


"""
You are going to write a program that calculates the sum of all the even numbers from 1 to X. 
If X is 100 then the first even number would be 2 and the last one is 100:
i.e. 2 + 4 + 6 + 8 + 10 ... + 98 + 100
Important, there should only be 1 print statement in your console output. 
It should just print the final total and not every step of the calculation.
Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.
"""

print("Calculate the sum of all Even Numbers. ")
target = int(input())
sumOfEvenNumbers = 0
for calc in range(0, target+1, 2):
    sumOfEvenNumbers += calc
print(sumOfEvenNumbers)


"""
You are going to write a program that automatically prints the solution to the FizzBuzz game. 
These are the rules of the FizzBuzz game:
Your program should print each number from 1 to 100 in turn and include number 100.
When the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
"""

print("Welcome to the FizzBuzz Game. ")
targett = 100
for number in range(1, targett + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


#Password Generator
import random
letters = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
symbols = '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '^', '_', '`', '{', '|', '}', '~'
numbers = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
print("Welcome to the PyPassword Generator! ")

in_letters = int(input("How many letters would you like in your password? \n"))
in_symbols = int(input("How many symbols would you like? \n"))
in_numbers = int(input("How many numbers would you like? \n"))

random_char = ""
for char in range(1, in_letters + 1):
    random_char += random.choice(letters)

for char in range(1, in_symbols + 1):
    random_char += random.choice(symbols)

for char in range(1, in_numbers):
    random_char += random.choice(numbers)
print(f"Here is your password: {random_char}")


#Another way
# password_list = []
# for char in range(1, in_letters + 1):
#     password_list += password_list.append(random.choice(letters))

# for char in range(1, in_symbols + 1):
#     password_list += password_list.append(random.choice(symbols))

# for char in range(1, in_numbers):
#     password_list += password_list.append(random.choice(numbers))

# print(f"Here is your password using append: {password_list}")
