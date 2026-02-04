''' This program demonstrates print(), data types, variables, inputs and f-strings '''

#print( ) is a function that outputs whatever is inside the brackets
# nmbers can be included directly in the berackets
print (1234)
print (1.5)
# When printing text, it must be in speechmarks which turns it into a string
print("Hello")

# There are lots of differebt data types:
# intergers, decimals (floating point numbers)
# text (string), boolean (true or false)


# we use variables to store information
# variables must be all lower case
# if you want multile words in the vaeriable name, use underscore
name = "Pluto"
first_name = "john"
last_name = "smith"
age = 14

# You can include variables inside print() statements
print(name)
# To combine variables witha a string, we use f-string
# The variable goes inside curly brackets{}
print(f"my dog is called (name) and he is {age} years old")
      
 # we use input() to get input from the user 
user_name = input ("what is your name?")
print(f"Hello {user_name}")
# print hello to the user and ask them how old they are
age = input ("what is your age")
print(f"hello {user_name}, your age is")

# Then print out their name and age