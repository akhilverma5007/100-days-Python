print("Welcome to the Roller Coaster Ride. ")
height = int(input("Tell us your height in cm? "))

if height > 120:
    print("You can ride the roller coaster. ")
    age = int(input("What's your age? "))
    if age < 12:
        print("You have to pay $5. ")
    elif age > 12 or age <= 18:
        print("You have to pay $7. ")
    elif age > 18:
        print("You have to pay $12. ")
    else:
        print("Sorry, Invalid age. ")
else:
    print("Ups, You can't ride the roller coaster. ")