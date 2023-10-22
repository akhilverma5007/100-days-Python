print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

split = int(input("How many people to split the bill? "))

solution = bill / 100
to_split_from = float((bill - solution * 10))

print(f"Each person should pay: ${float(to_split_from / split)}")



