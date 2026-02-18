'''Write a program that asks the user for a number. Then ask the user for a second number that is greater than the first. If it is not, the program should continue asking the user for a greater number until they successfully enter it. Then the program prints out the two numbers.'''
num1= int(input("Enter the first number: "))
num2= int(input("Enter second number that is greater than the first:"))
while num2 <= num1:
    print("The second number must be greater than the first number. Please try again.")
    num2= int(input("Enter second number that is greater than the first:"))
print(f"You entered {num1} and {num2}")
    


























