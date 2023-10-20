#Primitive Data Types: String, Integer, Float, Boolean

print(len("Hello"))
#print(len(1343))  -> This will produce error
print("Hello"[0])

#Concatinating
print("1234" + "5678")

#Integer
print(1234 + 5678)
print(123_456_789) #123456789 Large Integers

#Float
print(123.42)

#Boolean -> True, False

street_name = "Abbey Road"
print(street_name[4] + street_name[7])


#Operators
3 + 5
7 - 9
3 * 4
4 / 2
4 ** 2

#Precedence
# ()
# **
# * /
# + -

num_calc = (3 * 3 + 3 / 3 - 3)
print(type(num_calc))
new_num_calc = str(num_calc)
print("Calculation: " + new_num_calc)
#Solving
# 3 * 3 + 3 / 3 - 3
# 9 + 1 - 3
# 7
