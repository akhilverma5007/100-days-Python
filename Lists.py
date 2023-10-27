# List is a data structure used for storing data in python

fruits = ["apple", "orange", "banana"]
numbers = [1,2,3,4,5,6]
print(fruits)
print(numbers)

print(numbers[2])

#altering the list
numbers[1] = 34
print(numbers)

#adding to list
numbers.append(100)
print(numbers)

numbers.extend([20,40,60])
print(numbers)


# Nested Lists
fruits = ["apple", "banana", "orange", "grapes"]
vegetables = ["carrot", "patato", "tamatoes"]

combined_list = [fruits, vegetables]
print(combined_list)

fruits1 = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
print(fruits1[3])
print(fruits1[4])
print(fruits1[-5])
print(fruits1[-4])


fruits = ["apple", "banana", "orange", "grapes"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
