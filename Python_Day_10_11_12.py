# Functions With Outputs
def my_function():
    result = 3 * 2
    return result

output = my_function()
print(output) 

#String to Title Case in Python
def format_name(firstname, lastname): #Parameters as Input
    if firstname == "" or lastname == "":
        return "You didn't provide valid inputs."
    firstname = firstname.title()
    lastname = lastname.title()
    # print(f"{firstname} {lastname}")
    return f"{firstname} {lastname}"

# format_name("akhil", "VermA")
# print(format_name("akhil", "VermA"))

print(format_name(input("What is your first name? "), input("What is your last name? ")))


    
#Program - Days in Month
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1]
  

year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

#DocStrings
""" Comments in functions """
