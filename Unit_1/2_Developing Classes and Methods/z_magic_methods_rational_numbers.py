"""
Magic Methods (or dunder methods) allow programs to automatically call methods under specific conditions
without needing to reference them with the dot notation.

Operators such as '+' are implemented in Python as a magic method because they allow the program to use the same
addition symbol on a variety of data types such as integers, strings, and lists.

Another example, the __init__ method is a magic method because it is automatically called when an instance is created
in order to set the attributes of the instance.
"""

# x = 2
# y = 3

"""The examples below demonstrate operator overloading
    We define the '+' sign on three different data types to get different results
    
"""
#
# r1 = x + y # Result is 5
# r2 = str(x) + str(y) # Result is 23
# r3 = list(str(2)) + list(str(3)) # Result is ['2', '3'] since we added to lists together

# print(r1)
# print(r2)
# print(r3)

"""
    The __.add__() operator knows how to hande '+' based on the class that the variable comes from (int, str, or list)
    Remember - everything in Python is treated as an object, x=3 is an instance of the integer class
# """
# print(x.__add__(y)) # Use the .add operator instead of the '+' symbol
# print(x.__sub__(y))
# # print(str(x).__sub__(str(y))) # ERROR
# print(dir(str))

##################################################################################################################
""""
In this program we will define a class that allows us to perform operations with rational numbers. 

To do this we will define the magic methods that control how addition, subtraction, and then multiplication and division 
operations work.

    For example: if we define a rational number such as 1/2 and another suh as 1/3
    adding them together should output 3/2
"""

class RationalNumber:
    def __init__(self, numerator, denominator=1):
        self.n = numerator
        self.d = denominator

    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        numerator = self.n * other.d + self.d * other.n
        denominator = self.d * other.d

        # return f'{numerator}/{denominator}'
        return RationalNumber(numerator, denominator)



    def __sub__(self, other):

        numerator1, denominator1 = self.n, self.d
        numerator2, denominator2 = other.n, other.d

        result_numerator = (numerator1 * denominator2 - numerator2*denominator1)
        result_denomiantor = denominator1 * denominator2

        return RationalNumber(result_numerator, result_denomiantor)

    """"
    Exercise - Write __mul__ and __trudiv__ methods below
    """

    # Code for Exercise 2.5 goes here

    """
    Output as a rational number rather then a memory reference 
    """
    def __str__(self):
        return f'{self.n}/{self.d}'


if __name__ == "__main__":
    a = RationalNumber(1,2)
    b = RationalNumber(7, 6)

    print(a + b)

    print(a + 4)
    # print(isinstance(a, RationalNumber)) # True
    # print(isinstance(3, RationalNumber)) # False

    # print(3 + a)
    # print(a - 3)
