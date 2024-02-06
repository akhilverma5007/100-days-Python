#Data Types, Numbers, Operators, Type Conversion, f-Strings

#Primitive Data Types
print(len("abc"))
# print(len(1233)) (This produces error)

#1. Strings
name = "akhil"
print("Hello"[4])
print("123" + "456") #concatinating

#2. Integers
num = 102
print(123 + 456) #Integer summing 

#3. Large Integers
large_num = 342,654,896
largenum = 342_654_896
print(large_num)
print(largenum)

#4. Float
dec_num = 3.14159
print(dec_num)

#5. Boolean (True/False)
check = True
print(check)

#Type Error, Type Checking and Type Conversion

#Type Error
num_char = len(input("What is your name?"))
# print("Your name has " + num_char + "characters.") #Here we will get type error

#Type Checking
print(type(num_char))

#Type Conversion
new_num_char = str(num_char)
print(type(new_num_char))

print("Your name has " + new_num_char + " characters.")

print(10 + float("10.5"))

#Problem
"""
Write a program that adds the digits in a 2 digit number. e.g. if the input
was 35, then the output should be 3 + 5 = 8
Warning. Do not change the code on line 1. Your program should work for different inputs. e.g. any two-digit number.
The last line of your program should print the result.
"""

two_digit_number = input("Write a two digit number")
num0 = int(two_digit_number[0])
num1 = int(two_digit_number[1])
sum = int(num0 + num1)
str_sum = str(sum)
print(num0 + num1)

# str_num0 = str(num0)
# str_num1 = str(num1)
# print(str_num0 + " + " +  str_num1 + " = " + str_sum)

"""
Mathematical Operators
+
-
*
/
** exponent(power of number)

PRECEDENCE OF OPERATORS
()
**
* /
+ -

#PROB1
3 * 3 + 3 / 3 - 3 
9 + 1 - 3
10 - 3
7

#PROB2
3 * (3 + 3) / 3 - 3
3 * (6) / 3 - 3
18 / 3 - 3
6 - 3
3


"""

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)


#BMI Calculator
"""
Write a program that calculates the Body Mass Index (BMI) from a user's
weight and height.
BMI Wikipedia Page
The BMi is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
The BMI is calculated by
BMI = weight(kg) / height² (m²)
bmi = weight_kg / (height_m ** 2)
"""

weight = input("Enter your weight! ")
weight_kg = float(weight)

height = input("Enter your height in metres! ")
height_m = float(height)

bmi = weight_kg / (height_m ** 2)
print(type(bmi))

int_bmi = int(bmi)
str_bmi = str(int_bmi)
print(type(str_bmi))

print("Your BMI is " +  str_bmi)

"""eg: weight = 73, height = 0.14478 """

#Number Manipulation 
print(8 / 3)
print(round(8 / 3))
print(round(8 / 3, 2)) #upto 2 decimal places
print(type(4 / 2)) #Gives float
print(type(4 // 2)) #Gives int

example_output = 10 + 2
example_output += 2
print(example_output) #Should give 14

#F Strings in Python
score = 0
heightt = 1.8
isWinning = True
print(f"Your score is {score}, height is {heightt} and isWinning is {isWinning}.")

"""
Problem:
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
Warning your output should match the Example Output format exactly, even the positions of the commas and full stops."""

current_age = input("Enter your age? ")
int_current_age = int(current_age)
int_max_calculated_age = int(90)
int_left_age = int(int_max_calculated_age - int_current_age)

int_left_age_in_weeks = int_left_age * 52
print(f"You have {int_left_age_in_weeks} weeks left.")

#TIP CALCULATOR
print("Welcome to the tip calculator.\n")
total_bill = input("What was the total bill? $")
float_total_bill = float(total_bill)

tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
int_tip_percentage = int(tip_percentage)

people_to_split = input("How many people to split the bill? ")
int_people_to_split = int(people_to_split)

total_bill_adding_tip = float_total_bill * int_tip_percentage / 100
total_bill_adding_tip_conversion = total_bill_adding_tip + float_total_bill

final_output = total_bill_adding_tip_conversion / int_people_to_split
converted_final_output = round(final_output, 2)
print(f"Each person should pay: ${converted_final_output}")