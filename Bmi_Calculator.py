weight = input("Enter Your weight! ")
height = input("Enter Your height! ")

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)


