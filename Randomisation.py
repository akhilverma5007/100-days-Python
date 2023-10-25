#use randint(a, b) to choose randoms between and b

import random
import My_Module #importing another python file
print(My_Module.value)

random_integer = random.randint(100, 200)
print(random_integer)

#to create random float numbers
random_float = random.random()
print(random_float)

# How to create random float numbers between 0 and 5
random_float_0to5 = random.random() * 5
print(random_float_0to5)
