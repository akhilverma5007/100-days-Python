#Object Oriented Programming(OOP)
import moduleCheck.module

# from moduleCheck import module, pi

print(moduleCheck.module.pi)

#How to create a class
class Car: #Car is class name
    # user = Car() # user is object here

    def func():
        pass # to skip a empty functtion

# Cases
    #PascalCase
    #camelCase
    #snake_case

class User:
    pass
user_1 = User()
user_1.id = "001"
user_1.username = "akhil"

print(user_1.username)

#Constructor

def __init__(self):
    print("another user being created. ")