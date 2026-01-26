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

# Arithmetic
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

# Interesting thing not to dwell on
# n1 = 5
# some_number = 5
# print(n1 == some_number) # True
# print(n1 is some_number) # True
# print(id(n1), id(some_number))


# Logical
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
senors = [100, 200, 300]# List (mutable)
print(senors[1]) # Shows 200

senors[0] = 120 # Changes 100 to 120
print(senors)

senors.append(400) # add 400 to the end of the list
print(senors)

senors.insert(0, 'a_number')
print(senors)

# Tuple (immutable)





#------Concept 6: Conditionals -------
"""
    - Use if, elif, and else to make decisions
    - Conditions must evaluate to True or False
    - Use and, or, not to combine conditions
"""

temp = 22






#------Concept 7: Loops -------
"""
    - Use for loops to iterate through lists or ranges
    - Use while loops to repeat while a condition is true
    - Use break to exit, continue to skip one iteration
"""

# for loop with range



# for loop over list




# while loop





#------Concept 8: Functions -------
"""
    - Use def to define a function
    - Functions can take parameters and return values
    - Use return to send back a result
"""
# #No parameters passed



# #One (or more parameters passed)




#Using keyword parameters




#Using a return




# # Using type hints to indicate what data type Python should expect





#------Concept 9: Imports and Modules -------
"""
    - Use import to access standard or custom modules
    - You can import an entire module, specific functions, or use aliases
    - In ROS2, packages often import from subfolders using dot notation
"""

# # Import full module with all built-in function
pass
pass # call the function from the module using dot-notation



# Import specific function only




# # Import with alias, useful with modules that have long or awkward names




# Import multiple functions from a module