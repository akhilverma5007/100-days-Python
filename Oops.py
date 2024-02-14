# OOPS
# To map with real world scenarios, we started using objects in code.
# This is called object oriented programming

# Classes & Object in Python
# Class is a blueprint for creating objects.

#creating class
class Car:
    carName = "Maruti"

#creating object (instance)
s1 = Car()
print(s1.carName)

# __init__ Function
# Constructor (Being called every time a new object is created)
# All classes have a function called __init__(), which is always executed when the object is being initiated.

class Student:
    # Class & Instance Attributes
    # Class.attr
    # Obj.attr
    college_name = "Akhil coll" #Class Attribute
    name = "default name" #Class Attribute
    #default constructor
    def __init__(self):
        pass

    #parameterized constructors
    def __init__(self, name, marks): #self - FIrst Parameter #second parameter - name or anything
        self.name = name
        self.marks = marks
        print("adding new car in the database") 
    
    # Methods - Methods are functions that belong to objects
    # Non Static method used for objects, we use self
    def welcome (self):
        print("Welcome! ")

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class
s2 = Student("Akhil", 80)
print(s2.name, s2.marks)

s3 = Student("akhil", 88)
print(s3.name, s3.marks)

s4 = Student("Akhil", 10)
s4.welcome()
print(s4.welcome())

# Question - Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Studentt():
    def __init__(self):
        pass

    def __init__(self, studname, studmarks): #self - FIrst Parameter #second parameter - name or anything
        self.studname = studname
        self.studmarks = studmarks
    
    def get_average(self):
        sum = 0
        for val in self.studmarks:
            sum += val
        print("Hello", self.studname, "Your average score is:", sum/3)

stud = Studentt("Akhil", [90, 80, 70])
stud.get_average()

stud = Studentt("Tony", [40, 50, 30])
stud.get_average()
 

# Static Methods at class level
# Methods that don't use the self parameter (work at class level)

class AnotherStudentClass:
    @staticmethod #decorator
    def college():
        print("ABC College")

# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, 
# without permanently modifying it
        

# Important OOPS
"""
1. Abstraction
Hiding the implementation details of a class and only showing the essential features to the user.
2. Encapsulation
Wrapping data and functions into a single unit (object).
3. Inheritance
4. Polymorphism
"""