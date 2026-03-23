"""
Magic Methods (or dunder methods) allow programs to automatically call methods under specific conditions
without needing to reference them with the dot notation.

Operators such as '+' are implemented in Python as a magic method because they allow the program to use the same
addition symbol on a variety of data types such as integers, strings, and lists.

Another example, the __init__ method is a magic method because it is automatically called when an instance is created
in order to set the attributes of the instance.
"""

x = 2
y = 3

"""The examples below demonstrate operator overloading
    We define the '+' sign on three different data types to get different results
    
"""

pass # Result is 5
pass # Result is 23
pass # Result is ['2', '3'] since we added to lists together

"""
    The __.add__() operator knows how to hande '+' based on the class that the variable comes from (int, str, or list)
    Remember - everything in Python is treated as an object, x=3 is an instance of the integer class
"""
pass # Use the .add operator instead of the '+' symbol



##################################################################################################################
""""
In this program we will define a class that allows us to perform operations with rational numbers. 

To do this we will define the magic methods that control how addition, subtraction, and then multiplication and division 
operations work.

    For example: if we define a rational number such as 1/2 and another suh as 1/3
    adding them together should output 3/2
"""

class RationalNumber:
    pass


    """"
    Exercise - Write __mul__ and __trudiv__ methods below
    """

    # Code for Exercise 2.5 goes here

    """
    Output as a rational number rather then a memory reference 
    """



if __name__ == "__main__":
    pass
