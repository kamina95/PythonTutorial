#Variables and Data Types
#Variables are used to store data. A variable is a name that references a value. The value can be changed, as the name suggests.
#In Python, variables are created when a value is assigned to it. The value is assigned to the variable using the = operator.
#The value of a variable can be changed by assigning a new value to it.
#Variables can be of different types, such as int, float, string, and list.
#The type of a variable can be checked using the type() function.
#In Python, variables are case-sensitive.
#The value of a variable can be printed using the print() function.

#Example
#Create a variable named x and assign the value 5 to it. Then print the value of the variable.
x = 5
print(x)
#Output
#5


#Strings
#A string is a sequence of characters. It is a data type that is used to represent text.
#In Python, a string is defined using single quotes, double quotes, or triple quotes.
#The characters of a string can be accessed using their index. The index starts from 0.
#The length of a string can be obtained using the len() function.
#The characters of a string can be sliced using the slice notation.
#The + operator is used to concatenate two strings.
#The * operator is used to repeat a string a specified number of times.
#Example
#Create a string and print its characters and length.
text = "Hello, world!"
print(text)
print("Length:", len(text))
#Output
#Hello, world!
#Length: 13

#Example
#Access the characters of a string using their index.
text = "Hello, world!"
print(text[0])
print(text[7])
#Output
#H
#w

#Example
#Slice a string using the slice notation.
text = "Hello, world!"
print(text[0:5])
print(text[7:])
#Output
#Hello
#world!

#Example
#Concatenate two strings using the + operator.
text1 = "Hello, "
text2 = "world!"
print(text1 + text2)
#Output
#Hello, world!

#Example
#Repeat a string using the * operator.
text = "Hello, "
print(text * 3)
#Output
#Hello, Hello, Hello,

#String Methods
#A method is a function that is associated with an object. It is used to perform an operation on the object.
#In Python, a method is called using the dot notation, which consists of the object followed by the method name and the arguments in parentheses.
#The string object has many methods for working with strings, such as upper(), lower(), strip(), replace(), and split().
#Example
#Use the upper() method to convert a string to uppercase.
text = "Hello, world!"
print(text.upper())
#Output
#HELLO, WORLD!



#function
#A function is a block of code that performs a specific task. It takes input, processes it, and returns the output.
#In Python, a function is defined using the def keyword, followed by the function name and the parameters in parentheses.
#The function body is indented, and it contains the code that performs the task.
#A function can take zero or more parameters as input.
#A function can return a value using the return statement.
#A function can be called by using its name followed by the arguments in parentheses.
#Example
#Create a function named greet that takes a name as input and returns a greeting message.
def greet(name):
    return "Hello, " + name + "!"
#Call the function and print the returned value.
print(greet("John"))
#Output
#Hello, John!



#Global and Local Variables
#In Python, a variable can be either global or local.
#A global variable is defined outside of a function and can be accessed from anywhere in the program.
#A local variable is defined inside a function and can only be accessed from within that function.
#If a local variable has the same name as a global variable, the local variable takes precedence within the function.
#Example
#Create a global variable named x and a function that defines a local variable with the same name.
#The function prints the value of the local variable and the global variable.
x = 5
def my_function():
    x = 10
    print("Local variable:", x)
my_function()
print("Global variable:", x)
#Output
#Local variable: 10


#Lists
#A list is a collection of items. It is a mutable, ordered sequence of elements.
#In Python, a list is defined using square brackets [] and the elements are separated by commas.
#The elements of a list can be of different types, such as int, float, string, and list.
#The elements of a list can be accessed using their index. The index starts from 0.
#The elements of a list can be modified using their index.
#The length of a list can be obtained using the len() function.
#Example
#Create a list of numbers and print the elements and their length.
numbers = [1, 2, 3, 4, 5]
print(numbers)
print("Length:", len(numbers))
#Output
#[1, 2, 3, 4, 5]
#Length: 5

#Example
#Access the elements of a list using their index.
numbers = [1, 2, 3, 4, 5]
print(numbers[0])
print(numbers[3])
#Output
#1
#4

#Example
#Modify the elements of a list using their index.
numbers = [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers)
#Output
#[10, 2, 3, 4, 5]


#Dictionary
#A dictionary is a collection of key-value pairs. It is an unordered, mutable collection of items.
#In Python, a dictionary is defined using curly braces {} and the key-value pairs are separated by commas.
#The keys of a dictionary are unique and immutable, and they are used to access the values.
#The values of a dictionary can be of different types, such as int, float, string, list, and dictionary.
#The values of a dictionary can be accessed using their keys.
#The length of a dictionary can be obtained using the len() function.
#Example
#Create a dictionary of student names and their ages and print the elements and their length.
students = {"Alice": 20, "Bob": 21, "Charlie": 22}
print(students)
print("Length:", len(students))
#Output
#{'Alice': 20, 'Bob': 21, 'Charlie': 22}

#Loops
#A loop is a control structure that repeats a block of code multiple times.
#In Python, there are two types of loops: for loop and while loop.
#A for loop is used to iterate over a sequence of elements, such as a list or a string.
#A while loop is used to repeat a block of code as long as a condition is true.
#Example
#Create a for loop that iterates over a list of numbers and prints each number.
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
#Output
#1
#2...
#Example
#Create a while loop that repeats until a condition is false.
count = 0
while count < 5:
    print(count)
    count += 1
#Output
#0
#1...

#for loop and range()
#The range() function is used to generate a sequence of numbers.
#The range() function can take one, two, or three arguments.
#If one argument is provided, it generates a sequence of numbers from 0 to the specified number.
#If two arguments are provided, it generates a sequence of numbers from the first number to the second number.
#If three arguments are provided, it generates a sequence of numbers from the first number to the second number with the specified step.
#Example
#Use the range() function to generate a sequence of numbers.
for i in range(5):
    print(i)
#Output
#0
#1...
#Example
#Use the range() function to generate a sequence of numbers with a specified step.
for i in range(0, 10, 2):
    print(i)
#Output
#0
#2...


#Conditional Statements
#A conditional statement is a control structure that executes different code based on the evaluation of a condition.
#In Python, there are three types of conditional statements: if statement, if-else statement, and if-elif-else statement.
#An if statement is used to execute a block of code if a condition is true.
#An if-else statement is used to execute one block of code if a condition is true and another block of code if the condition is false.
#An if-elif-else statement is used to execute different blocks of code based on the evaluation of multiple conditions.
#Example
#Create an if statement that executes a block of code if a condition is true.
x = 5
if x > 0:
    print("Positive")
#Output
#Positive
#Example
#Create an if-else statement that executes one block of code if a condition is true and another block of code if the condition is false.
x = -5
if x > 0:
    print("Positive")
else:
    print("Negative")
#Output
#Negative
#Example
#Create an if-elif-else statement that executes different blocks of code based on the evaluation of multiple conditions.
x = 0
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
#Output
#Zero

#if statement and logical operators
#The and, or, and not operators are used to combine multiple conditions in an if statement.
#The and operator returns True if both conditions are true.
#The or operator returns True if at least one condition is true.
#The not operator returns True if the condition is false.
#Example
#Create an if statement that uses the and operator to combine two conditions.
x = 5
if x > 0 and x < 10:
    print("Between 0 and 10")
#Output
#Between 0 and 10
#Example
#Create an if statement that uses the or operator to combine two conditions.
x = -5
if x < 0 or x > 10:
    print("Less than 0 or greater than 10")
#Output
#Less than 0 or greater than 10
#Example
#Create an if statement that uses the not operator to negate a condition.
x = 5
if not x < 0:
    print("Not negative")
#Output
#Not negative

#Advance if statement
#The if statement can be used to check if a value is in a sequence using the in operator.
#The if statement can be used to check if a value is not in a sequence using the not in operator.
#Example
#Create an if statement that checks if a value is in a sequence.
numbers = [1, 2, 3, 4, 5]
if 3 in numbers:
    print("3 is in the list")
#Output
#3 is in the list
#Example
#Create an if statement that checks if a value is not in a sequence.
numbers = [1, 2, 3, 4, 5]
if 6 not in numbers:
    print("6 is not in the list")

#Shorter if statement
#The if statement can be written on a single line if it contains only one statement.
#Example
#Create an if statement that is written on a single line.
x = 5
if x > 0: print("Positive")

def is_adult(age):
    return True if age >= 18 else False
#Output
#Positive




#Classes and Object
#A class is a blueprint for creating objects. It defines the properties and behaviors of the objects.
#An object is an instance of a class. It is a concrete entity that has specific properties and behaviors.
#In Python, a class is defined using the class keyword, followed by the class name and a colon.
#The properties of a class are defined
#using variables called attributes.
#The behaviors of a class are defined
#using functions called methods.
#An object is created from a class using the class name followed by parentheses.
#Example
#Create a class named Person with attributes and methods.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return "Hello, my name is " + self.name + " and I am " + str(self.age) + " years old."
#Create an object of the Person class and call its methods.
person = Person("Alice", 20)
print(person.greet())
#Output
#Hello, my name is Alice and I am 20 years old.

#Modules
#A module is a file containing Python code. It can define functions, classes, and variables.
#In Python, a module can be imported into another module using the import statement.
#The import statement is followed by the name of the module to be imported.
#The functions, classes, and variables defined in the imported module can be accessed using the dot notation.
#Example
#Create a module named mymodule.py with a function and a variable.
#mymodule.py
#def greet(name):
#    return "Hello, " + name + "!"
#message = "Welcome to my module!"
#Import the mymodule module and call its functions and access its variables.
# import mymodule
# print(mymodule.greet("Alice"))
# print(mymodule.message)
#Output
#Hello, Alice!
#Welcome to my module!

#File Handling
#File handling is the process of reading from and writing to files on the disk.
#In Python, files can be opened using the open() function, which returns a file object.
#The file object has methods for reading from and writing to the file.
#The file object is closed using the close() method.
#Example
#Open a file and write to it using the write() method.
file = open("example.txt", "w")
file.write("Hello, world!")
file.close()
#Read from the file using the read() method.
file = open("example.txt", "r")
print(file.read())
file.close()
#Output
#Hello, world!

#Exception Handling
#Exception handling is the process of handling errors that occur during the execution of a program.
#In Python, exceptions are handled using the try-except block.
#The try block contains the code that may raise an exception.
#The except block contains the code that handles the exception.
#Example
#Create a try-except block that handles the ZeroDivisionError exception.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero!")
#Output
#Division by zero!

#Regular Expressions
#Regular expressions are patterns used to match character combinations in strings.
#In Python, regular expressions are supported by the re module.
#The re module provides functions for working with regular expressions, such as searching, matching, and replacing.
#Example
#Create a regular expression pattern that matches a sequence of digits.
import re
pattern = r"\d+"
text = "The price is $100"
match = re.search(pattern, text)
print(match.group())
#Output
#100

#Lambda Functions
#A lambda function is a small anonymous function that can have any number of arguments, but can only have one expression.
#In Python, lambda functions are defined using the lambda keyword, followed by the arguments and the expression.
#Lambda functions can be used as an argument to higher-order functions, such as map(), filter(), and reduce().
#Example
#Create a lambda function that adds two numbers.
add = lambda x, y: x + y
print(add(5, 3))
#Output
#8

#Map, Filter, and Reduce
#The map() function applies a function to each item in an iterable and returns a list of the results.
#The filter() function applies a function to each item in an iterable and returns a list of the items for which the function returns True.
#The reduce() function applies a function to each item in an iterable and returns a single value.
#Example
#Use the map() function to apply a function to each item in a list.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)
#Output
#[1, 4, 9, 16, 25]
#Example
#Use the filter() function to filter items in a list based on a condition.
numbers = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)
#Output
#[2, 4]
#Example
#Use the reduce() function to apply a function to each item in a list and return a single value.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)
#Output
#15

#List Comprehensions
#List comprehensions provide a concise way to create lists in Python.
#A list comprehension consists of square brackets containing an expression followed by a for clause and zero or more for or if clauses.
#Example
#Create a list of squares using a list comprehension.
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print(squared)
#Output
#[1, 4, 9, 16, 25]

#Generators
#A generator is a special type of iterator that can be used to iterate over a sequence of values.
#In Python, generators are defined using the yield keyword instead of the return keyword.
#Generators can be used to create iterators for large sequences of values without storing them in memory.
#Example
#Create a generator that yields the squares of numbers.
def squares(n):
    for i in range(n):
        yield i ** 2
for x in squares(5):
    print(x)
#Output
#0
#1
#4
#9
#16

#Decorators
#A decorator is a function that takes another function as an argument and returns a new function.
#In Python, decorators are defined using the @ symbol followed by the decorator function name.
#Decorators can be used to add functionality to existing functions without modifying their code.
#Example
#Create a decorator that adds a greeting message to a function.
def greeting_decorator(func):
    def wrapper(name):
        return "Hello, " + func(name) + "!"
    return wrapper
@greeting_decorator
def greet(name):
    return name
print(greet("Alice"))
#Output
#Hello, Alice!

#Context Managers
#A context manager is a Python object that is used to manage resources, such as files, network connections, and locks.
#In Python, context managers are defined using the with statement.
#The with statement is followed by a context manager expression, which returns a context manager object.
#The context manager object has methods for entering and exiting the context.
#Example
#Create a context manager that opens and closes a file.
with open("example.txt", "w") as file:
    file.write("Hello, world!")
#Output
#The file "example.txt" is created and contains the text "Hello, world!".

#Example
#Create a context manager that acquires and releases a lock.
import threading
lock = threading.Lock()
with lock:
    print("Locked")
#Output
#Locked

#Example
#Create a context manager that connects and disconnects from a network.
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("example.com", 80))
#Output
#The socket connects to the server "example.com" on port 80.


#Enum
#An enumeration is a set of symbolic names bound to unique values.
#In Python, enumerations are defined using the Enum class from the enum module.
#Enumerations can be used to create a set of named constants.
#Example
#Create an enumeration for the days of the week.
from enum import Enum
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
#Access the values of the enumeration.
print(Weekday.MONDAY.value)
#Output
#1