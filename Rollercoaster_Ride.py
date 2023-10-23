print("Hi welcome to the roller coaster ride!")
height = int(input("Please tell us your height? "))
if height > 120:
    print("You can ride the roller coaster. ")
    age = int(input("Please tell us your age? "))
    if age <= 18:
        print("Plese pay $7. ")
    else:
        print("Please pay $12. ")
else:
    print("Sorry can't ride. ")