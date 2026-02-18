'''Write a program that asks the user for two numbers then give a message telling them the two numbers they entered and tell them the larger number and the total'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"You entered {num1} and {num2}")  
if num1 > num2:
    print(f"The larger number is {num1}")
elif num2 > num1:
    print(f"The larger number is {num2}")
else:
    print("Both numbers are equal")
total = num1 + num2
print(f"The total of the two numbers is {total}")
