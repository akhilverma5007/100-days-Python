print("Welcome to the Bmi Calculator! ")

height = float(input("Tell us your height? "))
weight = int(input("Tell us your weight? "))

calulated_bmi = float(weight / height ** 2)

if calulated_bmi <= 18.5:
    print(f"Your bmi is: {calulated_bmi} and you're slightly underweight. ")
elif calulated_bmi > 18.5 and calulated_bmi < 25:
    print(f"Your bmi is: {calulated_bmi} and you have a normal weight. ")
elif calulated_bmi >= 25 and calulated_bmi < 30:
    print(f"Your bmi is: {calulated_bmi} and you're slightly oerweight. ") 
elif calulated_bmi >= 30 and calulated_bmi < 35:
    print(f"Your bmi is: {calulated_bmi} and you're obese. ")
elif calulated_bmi >= 35:
    print(f"Your bmi is: {calulated_bmi} and you're clinically obese. ")
else:
    print("Invalid Input. ")

