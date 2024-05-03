print("Hello World")
print('*'*10)

#variables
price =100        #int
weight = 1.5      #float
name = "apple"    #string
is_ripe = True    #boolean value
print(price)
print(weight)
print(name)
print(is_ripe)

#Receiving Input
name = input('Name of fruit: ')
color = input('color of fruit: ')
print(name + ' is ' + color)

#Type Conversion
#example 1
birth_year = input('Birth year: ')
age = 2024 - int(birth_year)          # int <- string
print(age)
#example 2
weight_lbs = input('Enter weight in pd: ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

#String
#Use of single quote
course = 'Python course for "Beginners"'
print(course)
#Use of double quotes
course = "python's course for Beginners"
print(course)
#Use of triple quotes
letter = '''
Hi michael,
This is your first paycheck.

Thanks
The Google Inc.
'''
print(letter)
#Display any character of a string
name = 'michael'
# print(name[-1])
#Display multiple characters of a string
print(name[0:3])
print(name[1:-1])          #print from second index till last index
#Displaying all character or cloning of a string
print(name[:])

#Formatted Strings
#example 1
first_name = 'Michael'
last_name = 'Bahik'
msg = first_name + ' [' + last_name + '] is a coder' # string concatenation
msg = f'{first_name} {last_name} is a coder'         #Formatted Strings
print(msg)
#example 2
year = 2023
event = 'welcome'
info = f'{event} proram of {year}'
print(info)

#String Methods 
# NOTE STRING IN PYTHON ARE CASE-SENSITIVE
# A.len() function : used to print the no of char present in a string ie. length of a string
course = 'Python Basics'
print(len(course))
# B.upper() function : used to print all characters of a sting in uppercase
course = 'Python Basics'
print(course.upper())
# C.lower() function : used to print all characters of a sting in lowercase
print(course.lower())
# D.find() fun:  used to print the index of any character
print(course.find('S'))        #display index that contain "s" at first ie.course[9] = s
print(course.find('basic'))    #display index of first char given in string ie.index of B
# E.replace() fun: used to replace the word with another
print(course.replace('Basics','for Beginners'))  
print(course.replace('Python','Java'))
# F. in operator : used to produce Boolean value
print('Python' in course)

# Arithematic Operations 
# six types of operators : add, subtract, multipy, divide, modulo and exponent
# add operator (+)
print(10 + 5)
# subtract operator (-)
print(10 - 5)
# multiply operator (*)
print(10 * 5)
# divide operator (/)
print(10 / 3)             #result is float value(3.33333)
print(10 // 3)            #result is integer value(3)
# modulo operator(%)
print(10 % 3)             #result is remainder(1)
# exponent operator (**)
print(10 ** 3)            #result is 1000
# augmented assignment operator (+=)
x = 10
x += 3       # x =  x + 3
y = 20
y -= x       # y = y - x
print(x)
print(y)

# Operator Precedence
# PEMDAS RULE CAN BE APPLIED (P = Parenthesis, E = Exponent, M = Multiplication, D = Division, A = Addition, S = Subtraction)
x = 10 + (3 * 2 ** 2)/3 - 5
print(x)

# Math Functions
# math module is available in python which provides access to the mathematical functions.
# A. round() fun : used to give round value of given number.
g = 9.8
print(round(g))
# B. abs() fun : used to give absolute value of given number.
x = -9
print(abs(x))
# Using Math Module
import math
print(math.ceil(2.9))
print(math.floor(3.4))
# Note : To learn more about math fun, search for python3 math module in GOOGLE

# Example 1
# If Statements
#     if it's hot
#       It's a hot day
#       Drink plenty of water
#     otherwise if it's cold
#       It's a cold day
#       Wear warm clothes
#     otherwise
#       It's a lovely day
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("drink Plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

# Example 2
# price of a house is $1M
# If buyer has good credit,
#     they need to put down 10%
# otherwise
#     they need to put down 20%
# print the down payment
price = 1000000
good_credit = True
if good_credit:
    down_payment = 0.1 * price 
else:
    down_payment = 0.2 * price 
print(f"Down Payment: ${down_payment}")

# Logical Operators
# Three types : and, or, not
# Example of 'and' operator
# If applicant has high income and good credit
# Eligible for loan
high_income = True
good_credit = True
if high_income and good_credit:
    print('Eligible for loan')
# Example of 'or' operator
high_income = True
criminal_record = False
if high_income or criminal_record:
    print("Eligible for loan")
# Example of 'not' operator
high_income = False
if not high_income:
    print("Eligible for loan")  

# Comparision Operator
# SIX TYPES: EQUAL TO(==0), NOT EQUAL TO(!=), GREATER THAN(>), GREATER THAN OR EQUAL TO(>=), LESS THAN(<), LESS THAN OR EQUAL TO(<=) 
# Example 1
# if temperature is greater than 30 
#     it's a hot day
# otherwise if it's less than 10
#     it's a cold day
# otherwise
#     it's neither hot or cold
temp = int(input())
if temp > 35:
    print("it's a hot day")
elif temp < 8:
    print("it's a cold day")
else:
    print("it's a normal day")
# Example 2
# if name is less than 3 character long
#     name must be at least 3 characters
# otherwise if its more than 50 characters long 
#     name can be a maximum of 50 characters
# otherwise 
#     name looks good
name = input()
if len(name) < 3:
    print("name must be atleast three characters")
elif len(name) > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good!")

# Weight converter Program
weight = input('Weight: ')
unit = input('(L)bs or (K)g: ')
if unit == "L":
    weight = float(weight) * (1/2.205)
    print(f'Weight in Kg: {weight}')
elif unit == "K":
    weight = float(weight) * 2.205
    print(f'Weight in Lbs: {weight}')
else:
    print("Wrong Input Unit")

# Loops
# While Loops
i = 1
while i <= 5:
    print(i)
    i = i + 1
print('Done')
# Guess Game Program
secret_no = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_no:
        print('You won!')
        break
else:
    print('You lose!')

# Building Simulation Car Game
command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped...")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit the game
              ''')
    elif command == "quit":
        print("Are you sure to quit the game?[y/n]: ")
        exit = input().lower()
        if exit == 'n':
            print("enter the command: ")
        elif exit == 'y':
            break
    else:
        print("Invalid command")
    
# For Loops
for item in [1,2,3,4]:
    print(item)
for fruit in ['apple', 'banana', 'mango', 'kiwi']:
    print(fruit)
for item in range(5,10):
    print(item)
prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f'total: {total}')   

# Nested Loops
# GENERATE LIST OF COORDINATES
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
#Generate pattern
#   *****
#   ****
#   ***
#   **
#   *
numbers = [5,4,3,2,1]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += '*'
    print(output)

# Generate pattern
#    *
#    *
#    *
#    *
#    * * * * *
numbers = [1,1,1,1,5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += '* '
    print(output)

# Generate pattern
#        *
#      * * *
#    * * * * *
#  * * * * * * *
n = int(input('enter n: '))
for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end=" ")
         
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end=" ")
        print('\n')

# Lists
names = ['john', 'bob', 'mike']
print(names[:])
# Write a program to find the largest number in a list.
numbers = [1, 2, 3, 4, 7, 5, 6]
print(max(numbers))

# 2D Lists:
# [ 
#    1 2 3 
#    4 5 6 
#    7 8 9
# ]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1])      # Access indiviual list
print(matrix[0][1])   # Access individual item
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:       # Print all items in 2D list
    for item in row:
        print(item)

# List Methods/ functions:
numbers = [2,3,1,6,8]
numbers.append(12)           # insert an element at the end of list
print(numbers)
numbers.insert(0, 10)        # insert an element(10) at 0 index value
print(numbers)
numbers.remove(numbers[2])   #remove an element of given index value from a list
numbers.remove(2)            # remove an element from a list
print(numbers)
numbers.clear()              # clear all elements from a list
print(numbers)
numbers.pop(3)               # pop an element from list and store 0 value
print(numbers)
print(numbers.index(8))      # display index value of the element
print(numbers.count(1))
numbers.sort()                 # arrange numbers in ascending order in a list
print(numbers)
print(numbers[1])
numbers.reverse()              # arrange elements in reverse order in a list
print(numbers)
numbers2 = numbers.copy()      # copy all elements of a list
print(numbers2)

# remove the duplicates in a list
list = [1,2,3,2,4,5,6,3,7,8,9,3,4]
uniques = []
for element in list:
    if element not in uniques:
        uniques.append(element)
print(uniques)

# Tuples - same like list but cannot be modified
numbers = (1, 2, 3)
print(numbers[0])
#number[0] = 10        # cannot change
# tuples are useful when we don't need to change item 

# Unpacking - powerful feature of python
coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
a = x + y + z
print (a)
x, y, z = coordinates     # Unpacking tuples into 3 variables
b = x + y + z + c
print(b)

# Dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# -> it is a structure used to store data values in key:value pairs 
# Name: Michael Bahik
# Email: michaelbahik75@gmail.com
# Phone: 9861757851
dev = {                           # curly braces are used
    "name": "Michael Bahik",
    "age": 23,
    "is_verified": True,
    "field": "Data Science"
}
dev["experience"] = "3"
print(dev)
print(dev["age"])
print(dev.get("sex"))      # o/p : None(which represents absence of value instead of error)
print(dev.get("sex", "male"))      # o/p : male(default value)
dev["field"] = "Machine Learning"
print(dev["field"])

# translate digit of a number into word
# ex: 1234 -> one two three four
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)   

# Emoji converter
message = input(">")
words = message.split(' ')  # split() fun: Return a list of the words in the string, using sep as the delimiter string.
emojis = {
    ":)": "😀",
    ":(": "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

# Functions
def greet_user():                    
    print("Hi there!")             # doesn't execute until fun is called
    print("Welcome to the cafe")   # doesn't execute until fun is called

print("Start")
greet_user()
print("Finish") 

# Parameters
def greet_user(name):              # PARAMETER: ARE PLACEHOLDR DEFINED IN A FUN FOR RECEIVING INFO              
    print(f"Hi {name}!")           # doesn't execute until fun is called
    print("Welcome to the cafe")   # doesn't execute until fun is called

print("Start")
greet_user("Mike")                 # ARGUMENT: ARE ACTUAL VALUES SUPPLIED TO THOSE FUNCTION
print("Finish") 

def user_info(fname, lname, age):
    print("User Details:")
    print("-----------------------")
    print(f'Name: {fname} {lname}')
    print(f'Age: {age}')
user_info(input(), input(), 23)
user_info(lname = input(), age = 23, fname = input())

#keyword Argument
def user_info(fname, lname, age):
    print("User Details:")
    print("-----------------------")
    print(f'Name: {fname} {lname}')
    print(f'Age: {age}')
user_info("Michael", "Bahik", "23")                          # Positional Argument
user_info(fname = "Michael", lname = "Bahik", age = "23")    # Keyword Argument  
# Note: while mixing keyword argument with positional argument, first positional argument must be used, then keyword argument.

# Return statements
def square(number):
    return number * number
print(square(3))

def square(number):
    print(number * number)
    return None # By default python return None value(absence of value)
print(square(3))

# Creating a Reusable function
def emoji_converter(message):
    words = message.split(' ')  # split() fun: Return a list of the words in the string, using sep as the delimiter string.
    emojis = {
        ":)": "😀",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output
message = input(">")
result = emoji_converter(message)
print(result)

# Exceptions 
age = int(input('Age: '))
print(age)
# Note: Exit code 0 means success
try:
    age = int(input('Age: '))  # this line will raise an exception in case of invalid value input 
    print(age)
except ValueError:             # this line will catch the above exception
    print('Invalid value')
# latent error(ZeroDivisionError)
try:
    num = int(input('num: '))
    rslt = num / 0;
except ZeroDivisionError:
    print("Cannot Divide by zero")

# Comments
# are identified with a hash symbol, #, and extend to the end of the line
# three ways to write a comment - as a separate line, beside the corresponding statement of code, or as a multi-line comment block
print("##")   # Hash characters in a string are not considered comments
name = '##'
print(name)
# ocean is blue    Note: This is bad comment
print("Ocean is blue")
# Note: Use comments only when it is necessary

# Classes
class Point:      # Pascal Naming convention Ex : FirstName
    def move(self):
        print("move")
    def draw(self):
        print("draw")
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()
point2 = Point()
point2.x = 1
print(point2.x)

# Constructors
#parameterized constructor takes its first argument as a reference
#to the instance being constructed known as self and the rest of              
#the arguments are provided by the programmer         
class Point:
    def __init__(self, x, y): 
      self.x = x
      self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")
point1 = Point("2","3")
print(point1.x)
print(point1.y)
point1.move()
point1.draw()


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def talk(self):
        print(f"Hi, I am {self.name}")
        print(f"I am {self.age} years old")
john = Person("John Smith", 21)
print(john.name)
john.talk()

mike = Person("Mike B", 20)
mike.talk()

michael = Person("Michael Bahik", 23)
michael.talk()

# Inheritance: DRY(DO NOT REPEAT YOURSELF) PRINCIPLE encourages us to not repeat lines of code.
class Mammal:
        def walk(self):       
            print("walk")


class Dog(Mammal):
    pass              # since python dont like empty class so pass means do nothing and just pass the line
    

class Cat(Mammal):
    def meow(self):
        print("meow meow")

 
dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.walk()
cat1.meow()

# Modules:a code library or a file that contains a set of functions
#can be imported inside another Python Modules Operations Program
import converters
from converters import kg_to_lbs

print(kg_to_lbs(100))
print(converters.lbs_to_kg(320))

from MaxNo import find_max

numbers = [10, 3, 2, 6]
max_value = find_max(numbers)
print(max_value)


# Packages: another way to organize our code
from ecommerce import shipping                 #method 1
shipping.calc_shipping()
from ecommerce.shipping import calc_shipping   #method 2
calc_shipping()
calc_shipping()

#  Generating Random Values
# all modules index
import random          #random.py is built-in module

for i in range(3):  
    print(random.randint(10,20))

members = ['John', 'Mary', 'Mike', 'Alice']
leader = random.choice(members)
print(leader)

import random
class Dice:     
    def roll(self, numbers):
        return random.choice(numbers)


numbers = ['1', '2', '3', '4', '5', '6']
roll = Dice()
print(roll.roll(numbers))

import random
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1,6)
        return first, second          # when we have to return tupple from fun we dont need to add parenthesis


dice = Dice()
print(dice.roll())
#Note : PEP8 is Python Enhancement proposals 8 used for formatting codes

#  Working With Directories
#Absolute path : /usr/local/bin (Linux)
#Relative path
from pathlib import Path
path = Path("ecommerce")
print(path.exists())

from pathlib import Path
path = Path("emails")
print(path.exists())
# print(path.mkdir)    -> create emails dir
# print(path.rmdir())  -> remove emails dir

path = Path()
# print(path.glob('*.py'))  -> Generator object
for file in path.glob('*.py'):
    print(file)

# PyPI and PIP
# PyPI.org has most useful packages
# finding from yelp.com
# openpyxl package install for working with excel files
# pip install openpyxl