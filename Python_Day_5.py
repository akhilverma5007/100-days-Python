#For Loops, Ramge and Code Blocks

fruits = ["apple", "banana", "orange", "chiku"]
for each in fruits:
    print(each)
    # print(each + "Pie")

print(len(fruits))

#Problem
"""
You are going to write a program that calculates the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
The average height can be calculated by adding all the heights together and dividing by the total number of heights.
"""

print("Welcome! Calculation of Average Student Height from a list of heights")
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[0])

totalHeight = 0
for height in student_heights:
    totalHeight += height    
print(f"total height = {totalHeight}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(totalHeight / number_of_students)
print(f"average height = {average_height}")