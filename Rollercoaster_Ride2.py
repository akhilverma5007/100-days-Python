print("Welcome to the Roller Coaster Ride")
height = int(input("What's your height? "))

if height > 120:
    print("Can ride.")
    age = int(input("What's your age."))
    wantphotos = input("Want Photos? Yes Or No? ")
   
    
    if age < 12 and wantphotos == "No":
        print("You have to pay +$5")
    if age < 12 and wantphotos == "Yes":
        print("You have to pay +$8")

    if age > 12 and age < 18 and wantphotos == "No":
        print("You have to pay +$7")
    if age > 12 and age < 18 and wantphotos == "Yes":
        print("You have to pay +$10")
    
    if age >= 18 and wantphotos == "No":
        print("You have to pay +$12")
    if age >= 18 and age < 45 and wantphotos == "Yes":
        print("You have to pay +$15")

    if age >=45 and age <= 55 and wantphotos == "Yes":
        print("You can ride for free.")
    if age >=45 and age <= 55 and wantphotos == "No":
        print("You can ride for free and take photos.")

else:
    print("Can't ride.")