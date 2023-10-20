#Type Error, Type Checking and Type Conversion
#num_char = print(len("What is your name? "))
#print("Hi your name has " + num_char + " characters.")

#THIS WILL GENERATE A TYPE ERROR

#Solution
num_char = input("What is your name? ")
length = len(num_char)

#Type Checking
print(type(num_char))
print(type(length))

#Type Conversion/Type Casting
print("Here Type Conversion Example Starts ")

num_char = len(input("What's Your Name? "))
new_num_char = str(num_char)

print(type(new_num_char))
print("Hi your name has " + new_num_char + " characters.")

float_num = float(100)
print(20 + float_num)


#Question
two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
print(type(two_digit_number))

index0 = int(two_digit_number[0])
index1 = int(two_digit_number[1])

print(index0 + index1)