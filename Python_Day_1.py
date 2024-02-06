#Printing, Commenting, Debugging, String Manupulation and Variables
# (Outputting the result)
print("Hello World!")
print("Hello'Akhil'")

#To write same output x3 
print("Hello World\nHello World!\nHello World")

#Concatinating Strings (Joing two strings)
print("Akhil" + "Verma")
print("Akhil " + "Verma")
print("Akhil" + " " + "Verma")

#Spaces are realy important in Python
#    print("akhil")
#This will produce an (Indentation Error)

#Debugging Practice
print("Day 1 - String Manipulation")
print("String Concatenation is done wit the "+" sign.")
# print("e.g. print('Hello ' + 'world')") 
print('e.g. print("Hello " + "world")') 
print("New lines can be created witha backslash and n.")

#input() function (Taking input from user)
output = input("What is your name? ")
print(output)

print("Hello " + input("What is your name? "))

#Print length of input 
print(len(input("")))

#Python Variables (Variables are containers for storing data values. Python has no command for declaring a variable)
name = input("What is your name? ")
print(name) #name is a Variable here

name = "Jack"
print(name)

print(len(name))

name = 10
print(name)

#Problem Statement
"""
This program takes two inputs. The first input is stored in a variable called
a. The second input is stored in a variable called b.
Write a program that switches the values stored in the variables a and b.
Warning. You don't need to print anything. The print statement is already in the template code. However, your program should work for different inputs. e.g. any value of a and b.
"""
a = input()
b = input()

temp = a
a = b
b = temp

print("a: " + a)
print("b: " + b)

#Problem Band-Name-Generator
print("Welcome to the Band Name Generator.")
city_name = input("What's the name of the city you grew up in? ")
print(city_name)

pet_name = input("What's your pet's name? ")
print(pet_name)

print("Your band name could be " + city_name + " " + pet_name)