userInput = int(input("Enter a number to check whether its a prime or not. "))
for i in range(2, userInput):
    if userInput % i == 0:
        print("Not a prime number. ")
    else:
        print("Its a prime number. ")