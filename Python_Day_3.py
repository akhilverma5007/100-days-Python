#Conditional Statements, Logical Operators, Code Blocks and Scope
#IF ESLE STATEMENT
"""
if condition:
    do this
else:
    do this
"""

#Problem of a bathtub 
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue ")

#Problem Rollercoaster Ride
print("Welcome to the Rollercoaster Ride. ")
height = int(input("Tell us your height! "))
if height >= 120:
    print("Can Ride.")
else:
    print("Can't Ride.")


#Comparision Operators
"""
    >     Greater than
    <     Less than
    >=    Greater than or equal to
    <=    Less than or equal
    ==    Equal to
    !=    Not Equal to
"""

#Logical Operators
"""
A and B 
C or D
not E
"""

"""
Write a program that works out whether if a given number is an odd or even number.
Even numbers can be divided by 2 with no remainder.
e.g. 86 is even because 86 ÷ 2 = 43
43 does not have any decimal places. Therefore the division is clean.
e.g. 59 is odd because 59 ÷ 2 = 29.5 A
29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
"""

print("Welcome! ")
userInput = int(input("Please input a number to check whether its even or odd!"))
if userInput % 2 == 0:
    print("You've typed an Even Number. ")
else:
    print("You've typed an Odd Number. ")

#NESTED IF ELSE STATEMENTS 
"""
if condition:
    if another condittion:
        do this
    else:
        do this
else:
    do this
"""    
    
print("Welcome to the RollerCoaster Ride Again. ")
heightRecheck = int(input("Plese tell us your height? "))
ageRecheck = int(input("Please tell us your age? "))
if heightRecheck >= 120:
    print("You can Ride.")
    if ageRecheck <= 18:
        print("You are eligible and you've to pay $7. ")
    else:
        print("You are eligible and you've to pay $12. ")
else:
    print("Sorry! You're not eligible. ")


#ELIF STATEMENTS
print("Welcome to the RollerCoaster Ride 3rd Time. ")
heightRecheckAgain = int(input("Please let us know your height? "))
ageRecheckAgain = int(input("Please let us know your age? "))
if heightRecheckAgain > 120:
    print("You can ride. ")
    if ageRecheckAgain < 12:
        print("You have to pay $5.")
    elif ageRecheckAgain > 12 and ageRecheckAgain < 18:
        print("You have to pay $7.")
    elif ageRecheckAgain > 18:
        print("You have to pay $12.")
else:
    print("You cannot ride. ")


"""
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
• Under 18.5 they are underweight
• Over 18.5 but below 25 they have a normal weight
• Over 25 but below 30 they are slightly overweight
• Over 30 but below 35 they are obese
• Above 35 they are clinically obese.
"""

print("Welcome to the BMI Calculator. ")
userHeight = float(input("Please tell us your height in metres? "))
userWeight = int(input("Please tell us your weight in kg? "))

userBmi = userWeight / (userHeight * userHeight)
print(type(userBmi))
print(userBmi)

if userBmi < 18.5:
    print(f"Your Bmi is {userBmi} and You're underweight. ")
elif userBmi > 18.5:
    print(f"Your Bmi is {userBmi} and You've a normal weight. ")
elif userBmi > 25 and userBmi < 30:
    print(f"Your Bmi is {userBmi} and You're slightly overweight. ")
elif userBmi > 30 and userBmi < 35:
    print(f"Your Bmi is {userBmi} and You're obese. ")
elif userBmi > 35:
    print(f"Your Bmi is {userBmi} and You're clinically obese. ")


"""
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, 
with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice.
This is how you work out whether if a particular year is a leap year.
• on every year that is divisible by 4 with no remainder
• except every year that is evenly divisible by 100 with no remainder
• unless the year is also divisible by 400 with no remainder
If english is not your first language or if the above logic is confusing, try using this flow chart.
So the year 2000 is a leap year.
But the year 2100 is not a leap year because:
2100÷ 4= 525 (Leap)
2100 ÷ 100 = 21 (Not Leap)
2100 ÷ 400 = 5.25 (Not Leap)
Warning your output should match the Example Output format exactly, including spelling an punctuation.
e.g. The year 2000:
2000÷ 4= 500 (Leap)
2000 ÷ 100 = 20 (Not Leap)
2000÷ 400= 5 (Leap!)
So the year 2000 is a leap year.
But the year 2100 is not a leap year because:
2100÷ 4= 525 (Leap)
2100 ÷ 100 = 21 (Not Leap)
2100 ÷ 400 = 5.25 (Not Leap)
Warning your output should match the Example Output format exactly, including spelling an punctuation.
"""

print("Welcome to the the Program to check Leap Year.")
year = int(input("Enter Year you want to check? "))
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap year.")



#Roller Coaster With Height, Age, Photgraph Allowance
print("Welcome to the Roller Coaster With Height, Age, Photgraph Allowance! ")
heightR = int(input("Tell us your height? "))
bill = 0

if heightR >= 120:
    print("You can Ride.")
    ageR = int(input("What's Your age? "))
    if ageR < 12:
        bill = 5
        print("You have to pay $5. ")
    elif ageR > 12 and ageR <= 18:
        bill = 7
        print("You have to pay $7. ")
    else:
        bill = 12
        print("You have to pay $12")
   
    wantPhotograph = input("Do you want photograph? ")
    if wantPhotograph == "Yes":
        bill += 3
        print(f"You have to pay +$3. Your final bill is ${bill}")
   
else:
    print("You cannot Ride.")


#Pizza Order
"""
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizzalY or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
"""

print("Hi Welcome! to the Pizza Outlet.\n")
pizza = str(input("Please place your order S-Small Pizza, M-Medium Pizza, L-Large Pizza "))
pepperoni = str(input("Add Pepperoni Y Or N "))
extraCheese = str(input("For Extra cheese chosse Y or N. "))

pizzaBill = 0
if pizza == 'S' and pepperoni == 'N' and extraCheese == 'N':
    pizzaBill = 15
    print(f"ThankYou For choosing Pizza From Us.\nYour Final bill is: ${pizzaBill}.")
elif pizza == 'S' and pepperoni == 'Y' and extraCheese == 'N':
    pizzaBill = 17
    print(f"ThankYou For choosing Pizza From Us.\nYour Final bill is: ${pizzaBill}.")
elif pizza == 'S' and pepperoni == 'Y' and extraCheese == 'Y':
    pizzaBill = 18
    print(f"ThankYou For choosing Pizza From Us.\nYour Final bill is: ${pizzaBill}.")

elif (pizza == 'M') or (pizza == 'L') and pepperoni == 'N' and extraCheese == 'N':
    pizzaBill = 20
    print(f"ThankYou For choosing Pizza From Us.\nYour Final bill is: ${pizzaBill}.")
elif (pizza == 'M') or (pizza == 'L') and pepperoni == 'Y' and extraCheese == 'N':
    pizzaBill = 23
    print(f"ThankYou For choosing Pizza From Us.\nYour Final bill is: ${pizzaBill}.")
elif (pizza == 'M') or (pizza == 'L') and pepperoni == 'Y' and extraCheese == 'Y':
    pizzaBill = 24
    print(f"ThankYou For choosing Pizza From Us.\nYour Final bill is: ${pizzaBill}.")

else:
    print("Invalid Input. ")  

#Love Calculator
print("The love calculator is calculating your score...")
name1 = input("What's your name? ")
name2 = input("What's thier name? ")

combined_names = (name1 + name2).lower()

t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
first_digit = t + r + u + e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if(score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif(score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
