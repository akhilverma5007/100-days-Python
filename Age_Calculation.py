#Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

#It will take your current age as the input and output a message with our time left in this format:

#You have x weeks left.
#Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

#Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.


# age_lived = input("Type Your age? ")
# int_age_lived = int(age_lived)

# days_lived = int_age_lived * 365

# weeks_lived = days_lived / 7
# int_weeks_lived = int(weeks_lived) #Weeks lived 

# total_days = 90 * 365

# total_weeks = total_days / 7
# int_total_weeks = int(total_weeks)

# final_output = total_weeks - weeks_lived

# int_final_output = int(final_output)

# print(f"You have {int_final_output} weeks left.")


age = input()
years = 90 - int(age)
weeks = years * 52
print(f"You have {weeks} weeks left.")


# print(6 + 4 / 2 - (1 * 2))

# 6 + 4 / 2 - (1 * 2)
# 6 + 4 / 2 - 2
# 6 + 2 - 2
# 8 - 2
# 6

# a = int("5") / int(2.7)
# a = 5 / 2











