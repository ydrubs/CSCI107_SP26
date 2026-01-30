#------Concept 1: Docstrings and Comments -------
"""
    - Docstrings are declared with triple quotation marks
    - Docstrings describe what a script or function does
    - Use them at the beginning of a file or inside a function
    - Use comments (#) to explain code or disable lines during testing
"""

"""
Docstring comments appear in a different shade when they are not part of the first line
"""
# A single-line comment example
a = 1  # This is an inline comment



#------Concept 2: Input / Output -------
"""
    - Use print() to output text to the terminal
    - Use input() to get user input — input() always returns a string
    - Use int(), float(), or str() to convert input types
    - Use f-strings for clean output formatting
"""
# name = input("Enter your name: ")
# age = input("Enter your age: ")
#
# print(f"Hello {name}, you are {age} years old.")
# print("In 5 years you will be" , int(age) + 5)
# print("In 5 years you will be " + str(int(age) + 5) + " years old")


#------Concept 3: Variable Assignment -------
"""
    - Use = to assign a value to a variable
    - Use compound operators (e.g., +=, *=) to update values
    - Variable names should be descriptive
    - Python variables can change type, but use consistently
"""

x = 5
x = x + 2  # x is now 7
name = 'Bob'
status = True
print(type(x), type(name), type(status)) # Python is strongly-typed


#------Concept 4: Operators -------
"""
    - Arithmetic: +, -, *, /, %, //, **
    - Comparison: ==, !=, <, >, <=, >=
    - Logical: and, or, not
    - Assignment: =, +=, -=, *=, etc.
"""

# -- Arithmetic
# a = 10 + 5 # addition
# b = 10 % 4 # modulus (remainder)
# c = 4 ** 2# Exponents
# print(c)
# number = 9
# other_number = 10
# print(number/other_number) # / Always results in a float
# print(number//other_number) # Always gives an integer ROUNDED DOWN

#
# d = 100 ** 0.5
# print(d)

# # Comparison
# print(a == 15)     # True
# print(a != 14)     # True


"""
Python handles storing data in memory differently depending on the value of the data
"""
# -- Python creates the same data piece for both so it places it in the same location in memory
# a = 1
# b = 1

# -- Python does a different set of operation so it treats them as two district pieces of data
# c = 5000
# d = int(str(5000))
#
# print(a is b) # TRUE
# print(c is d) # FALSE

# -- Lists are always distict pieces of data
# l1 = [1,2,3]
# l2 = [1,2,3]

# print(l1 is l2) # FALSE



# -- Logical
# temperature = 25
# print(temperature > 20 and temperature < 30)  # True
# print(temperature > 20 and not temperature > 30) # True



#------Concept 5: Data Types -------
"""
    - int, float, str, bool are basic types
    - list and tuple store multiple values
    - Use type() to check a variable’s type
"""

a = 42          # int
b = 3.14        # float
c = "robot"     # str
d = True        # bool

"""
    A MUTABLE data type means that an element in the data type can be 
    changed without overwriting the entire data set
        Example: In the list [0,1,2,3]
                 ...we can change the 0 to a 10 without creating a new list
    
    An IMMUTABLE data type means that we cannot change an element in a 
    data type unless we overwrite the entire data 
        Example: In the string "Hello", we cannot change the 
                  'H' to a 'Y' without rewriting the string completely 
"""
# senors = [100, 200, 300]# List (mutable)
# print(senors[1]) # Shows 200
#
# senors[0] = 120 # Changes 100 to 120
# print(senors)
#
# senors.append(400) # add 400 to the end of the list
# print(senors)
#
# senors.insert(0, 'a_number')
# print(senors)
#
#
# senors.pop()
# print(senors)
#
# senors.pop(1)
# print(senors)



# Tuple (immutable)
# position = (5, 10, 15)
# print(position[1]) # Tuples are iterable
#
# for thing in position:
#     print(thing)

# position[0] = 6 # Can't overide individual elements

# print(dir(position))
# print(help(int))
#
#


#------Concept 6: Conditionals -------
"""
    - Use if, elif, and else to make decisions
    - Conditions must evaluate to True or False
    - Use and, or, not to combine conditions
"""
# temp = 22
# if temp > 30:
#     print("it's hot")
# elif temp >= 20:
#     print("Its warm")
# else:
#     print("System ready")

#------Concept 7: Loops -------
"""
    - Use for loops to iterate through lists or ranges
    - Use while loops to repeat while a condition is true
    - Use break to exit, continue to skip one iteration
"""
colors = ['green', 'red', 'black', 'dark_red']

# for loop with range (looping by positon of element)
# for i in range(5): #Range is exclusive
#     print(i)
#
# for i in range(2, 10):
#     print(i)

# for i in range(2,100,2):
#     print(i)

# for i in range(len(colors)):
#     print(-i, colors[-i])


# for loop over list
# for color in colors:
#     print(color)
#     if color == 'red':
#         print("I like red too!")
#         break
#         # continue


# while loop
# x = 0
# while x <= 11:
#     print(f"x is {x}")
#     x +=1
#
# y = 0
# while True:
#     print(f"y is {y}")
#     y +=1
#     if y == 11:
#         break





#------Concept 8: Functions -------
"""
    - Use def to define a function
    - Functions can take parameters and return values
    - Use return to send back a result
"""
# #No parameters passed
# def greet():
#     print("Hello")
# greet()

# def greet():
#     return "hello"
#
# greeting = greet()
# print(greeting) # prints hello
#
# print(greet()) # also prints hello

# #One (or more parameters passed)
# def greet(name : str):
#     return f"hello {name}"

# user_name = input("Enter your name: ")
# greeting = greet("Jon")
# print(greeting)

# def greet(name : str, age : int) -> int:
#     n = age + 10
#     return n
#
# greeting = greet('Jon', 20)
# print(greeting)


# Using keyword parameters
def greet(name : str = 'Jon', age : int = 20) -> tuple:
    return f"Hello {name} you are {age} years old"
    # return (name, age)

greeting = greet('Bill', 45)
print(greeting)

another_greeting = greet(age = 50)
print(another_greeting)

# Positional parameters NEED to be used first if there both keyword and postional
def greet(location: tuple, name : str = 'Jon', age : int = 20):
    profile = [name, age, location]
    return  profile

coordinates = (3.456245, 45.387338)
a_profile = greet(coordinates)
print(a_profile)
print(f"You are located at the x-coordinate of {a_profile[2][0]}"
      f"and the y-coordinate of {a_profile[2][1]}")




#------Concept 9: Imports and Modules -------
"""
    - Use import to access standard or custom modules
    - You can import an entire module, specific functions, or use aliases
    - In ROS2, packages often import from subfolders using dot notation
"""

# # Import full module with all built-in function
import math
result = math.sqrt(2) # call the function from the module using dot-notation
print(result)

# Import specific function only
from math import sqrt, pi

result2 = sqrt(2)
print(pi)

# # Import with alias, useful with modules that have long or awkward names
from math import sqrt as i_love_math
print(i_love_math(4))

import random as i_have_no_idea_what_is_going_on
n = i_have_no_idea_what_is_going_on.randint(0,100)
print(n)


# Import multiple functions from a module
from math import *
result3 = sqrt(25)
print(result3)

# --- in - class practice ---
# --- return the first occurence of a letter in a word
word = 'PProgramming'
word = list(word)
word_copy = list(word)

occurences = 0
for letter in word:
    if letter in word_copy:
        occurences +=1
        if occurences > 1:
            print(letter)
            break

word2 = "programming"
for letter in word2:
    if word2.count(letter) > 1:
        print(letter)
        break