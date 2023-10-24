height = int(input("Tell us your height in cm! "))
# print(height)
# if else condition
if height > 120:
    print("Can ride.")
else:
    print("Can't ride.")


# nested if else condition
num1 = int(10)
num2 = int(20)

if num1 + num2 == 30:
    if(num1 == 20):
        print(f"num1 is {num1}")
    else:
        print("Invalid")

else:
    print(f"{num2}")


# if / elif / else condition (ONLY 1 Will be Executed)
# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do C

# Multiple if (If ALL Three are true, all three will be executed)
# if condition1:
#     do A
# if condition2:
#     do B
# if condition3:
#     do C

