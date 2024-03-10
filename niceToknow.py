#method to get input from user
#input()
# like this:
# name = input("Enter your name: ")

#ramdom library#
#The random module provides functions for generating random numbers.
#The randint() function returns a random integer between the specified range.
#The choice() function returns a random element from the specified sequence.
#The shuffle() function shuffles the elements of a list.
#Example
#Generate a random number between 1 and 10.
import random
print(random.randint(1, 10))
#Output
#8
#Example
#Select a random color from a list of colors.
colors = ["red", "green", "blue", "yellow"]
print(random.choice(colors))
#Output
#blue


#print with {} and format
#The format() method is used to insert values into a string.
#The {} placeholders in the string are replaced with the values passed to the format() method.
#The values can be passed as positional arguments or keyword arguments.
#Example
#Insert a name and an age into a string using positional arguments.
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
#Output
#My name is John and I am 30 years old.

#print with {} and f
#The f-string is a string literal that allows you to embed expressions inside curly braces {}.
#The expressions inside the curly braces are evaluated and replaced with their values.
#The f-string starts with the letter f or F before the opening quotation mark.
#Example
#Insert a name and an age into a string using f-string.
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
#Output
#My name is John and I am 30 years old.


#isInstance() method
#The isinstance() method is used to check if an object is an instance of a specified class or type.
#The method returns True if the object is an instance of the specified class or type, otherwise False.
#Example
#Check if the value is an instance of the int class.
value = 10
print(isinstance(value, int))
#Output
#True
#Example
#Check if the value is an instance of the float class.
value = 10.5
print(isinstance(value, float))
#Output
#True

#data types conversion
#The int() function converts a string or a float to an integer.
#The float() function converts a string or an integer to a float.
#The str() function converts an integer or a float to a string.
#Example
#Convert a string to an integer.
number = int("10")
print(number)
#Output
#10
#Example
#Convert a string to a float.
number = float("10.5")
print(number)
#Output
#10.5

#arithmatic operations
#The + operator is used to add two numbers.
#The - operator is used to subtract one number from another.
#The * operator is used to multiply two numbers.
#The / operator is used to divide one number by another.
#The % operator is used to get the remainder of a division.
#The // operator is used to get the integer division result.
#The ** operator is used to raise a number to the power of another number.
#Example
#Add two numbers.
result = 10 + 5
print(result)
#Output
#15
#Example
#Subtract one number from another.
result = 10 - 5
print(result)
#Output
#5
#Example
#Multiply two numbers.
result = 10 * 5
print(result)
#Output
#50
#Example
#Divide one number by another.
result = 10 / 5
print(result)
#Output
#2.0
#Example
#Get the remainder of a division.
result = 10 % 3
print(result)
#Output
#1
#Example
#Get the integer division result.
result = 10 // 3
print(result)
#Output
#3
#Example
#Raise a number to the power of another number.
result = 10 ** 3
print(result)
#Output
#1000

#comparison operators
#The == operator is used to check if two values are equal.
#The != operator is used to check if two values are not equal.
#The < operator is used to check if one value is less than another.
#The > operator is used to check if one value is greater than another.
#The <= operator is used to check if one value is less than or equal to another.
#The >= operator is used to check if one value is greater than or equal to another.
#Example
#Check if two values are equal.
result = 10 == 5
print(result)
#Output
#False
#Example
#Check if two values are not equal.
result = 10 != 5
print(result)
#Output
#True
#Example


