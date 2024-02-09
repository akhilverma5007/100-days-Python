#The Python Dictionary

programming_dictionary = {
    "Bug": "An error occoured. ",
    "Function": "A piece of code. ",
    "Loop": "The action of doing something continuously. ",
    9899: 98999999999}
    
#Retrieving items via key from dictionary
print(programming_dictionary["Bug"])
print(programming_dictionary[9899])

programming_dictionary["add_another_key"] = "New key can also be added like this."

#Printing the dictionary
print("Printing Dictionary:\n", programming_dictionary)

#Redefining/Editing an existing item
programming_dictionary["Bug"] = "Editied by line no 19"
print("Printing Dictionary:\n", programming_dictionary)

#Creating an empty dictionary
empty_dict = {}

#Wiping an existing dictionary
# programming_dictionary = {}
# print("Printing Dictionary:\n", programming_dictionary)

for dict in programming_dictionary:
    print("key ",dict)


#Problem
"""
You have access to a database of student_scores in the format of a dictionary. 
The keys in student_scores are the names of the students and the values are their exam scores.
Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary 
called student_grades that should contain student names for keys and their grades for values.

The final version of the student_grades dictionary will be checked.
This is the scoring criteria:
Scores 91 - 100: Grade = "Outstanding"
Scores 81 - 90: Grade = "Exceeds Expectations"
Scores 71 - 80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Fail"
"""

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for grade in student_scores:
    score = student_scores[grade]
    if score > 90:
        student_grades[grade] = "Outstanding"
    elif score > 80:
        student_grades[grade] = "Exceeds Expectations"
    elif score > 70:
        student_grades[grade] = "Acceptable"
    elif score <= 70:
        student_grades[grade] = "Fail"
         

print(student_grades)


# Nesting Lists
"""
{
    key: [List],
    key2: {Dict},
}
"""

#Nesting a List in a Dictionary
nested_dict = {
    "key1": ["abc", "cde", "fgh"],
    "key2": ["a", "b", "c"],
}
print(nested_dict)

#Nesting Dictionary in a Dictionary
travel_log1 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
print(travel_log1)

#Nesting Dictionary in a List
travel_log2 = [
    {
    "country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
    },
    {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5,
}]

print(travel_log2)