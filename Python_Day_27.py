list_of_strings = input().split(',')

numbers = [int(x) for x in list_of_strings]

result = [num for num in numbers if num%2 == 0]

print(result)