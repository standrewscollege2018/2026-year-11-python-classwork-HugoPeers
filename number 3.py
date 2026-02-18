'''Write a program to ask the user for numbers between 50 and 100 and to keep adding them to the total. The program should stop adding and print out the grand total once the total is bigger than 200.'''
total = 0
while total <= 200:
    num = int(input("Enter a number between 50 and 100: "))
    if num < 50 or num > 100:
        print("Invalid input. Please enter a number between 50 and 100.")
        continue
    total += num
print(f"The grand total is {total}")    





















'''Write a program to ask the user for numbers between 50 and 100 and to keep adding them to the total. The program should stop adding and print out the grand total once the total is bigger than 200.'''
total=0
while total <=200:
    num = int(input("Enter a number between 50 and 100: "))
    if num < 50 or num > 100:
        print("Invalid code nobhead try again")
        num = int(input("Enter a number between 50 and 100:"))
        continue 
    total += num
    if total > 200:
        print (f"The grand total of this stufff is {total}")
        break