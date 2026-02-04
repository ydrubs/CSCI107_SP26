"""0.1 - List Comprehension

List comprehension in Python is a concise way to create lists from existing ones.
It's a powerful tool to write cleaner, more readable code

"""

###########################################################
"""Create a list of values from 0 to 99 using a for loop"""
# numbers = []
# for i in range(100):
#     numbers.append(i)
#
# print(numbers)


"""Use list comprehension to achieve the same thing"""
# numbers = [i for i in range(100)]
# print(numbers)

###########################################################
"""Filtering - Create a list of only even numbers between 0 and 99 using a for loop"""
# evens = []
#
# for i in range(100):
#     if i % 2 == 0:
#         evens.append(i)
# print(evens)



"""Filtering - Create a list of only even numbers between 0 and 99 using list comprehension"""
# evens = [i for i in range(100) if i % 2 == 0]
# print(evens)



###########################################################
"""Mapping - Create a list that doubles every number between 0 and 99 using a for loop"""
# double = []
# for i in range(100):
#     i *= 2
#     double.append(i)
# print(double)



"""Mapping - Create a list that doubles every number between 0 and 99 using list comprehension"""
# double = [i*2 for i in range(100)]
# print(double)
#



###########################################################
"""Combining mapping and filtering with a loop.
Triple all the even numbers between 1 and 100"""
# triple = []
# for i in range(100):
#     i *= 3
#     if i % 2 == 0:
#         triple.append(i)
#
# print(triple)


"""Combining mapping and filtering with list comprehension
Triple all the even numbers between 1 and 100 and only put them in if they are even"""
triple = [i*3 for i in range(100) if i % 2 == 0]
print(triple)


###########################################################

"""Using list comprehension to filter common elements of two lists
First we'll make two lists - multiples of 3 and 5 up tp 100 using list comprehension"""
# threes = [i for i in range(100) if i % 3 == 0]
# fives = [i for i in range(100) if i % 5 == 0]
# print(threes)
# print(fives)

"""Now we use a for loop to filter the common elements in both lists and write to a new list"""
# common_multiples = []
# for number in threes:
#     if number in fives:
#         common_multiples.append(number)
# print(common_multiples)


"""...using list comprehension to do the same"""
# common_multiples = [i for i in threes if i in fives]
# print(common_multiples)
#
# colbys_numbers = [15, 75, 67]
# common_multiples2 = [i for i in threes if i in fives and i in colbys_numbers]
# print(common_multiples2)

###########################################################

"""
Whole-class example - 
    “Digital Root” Repeater - given an integer, keep summing the digits until one integer remains 
            Example - 99 -> 18 -> 9 (outpus 9)
            
                Input: a whole number (ex: 472)
                Output: keep summing digits until one digit remains (ex: 4)
                
        Process:
            1) recast int, n, into a string
            2) recast that string into a list of character
            3) Convert each character back into an int
            4) take the sum of each element from the list
"""

###########################################################
# n = 67
#
# n_sum = sum([int(i) for i in str(n)])
# print(n_sum)


"""
    Try it:
    First Letter Extractor:
        Write a list comprehension that takes a list of words and returns a list containing only the first letter of each word.

        Example: words = ["apple", "banana", "cherry", "ambarella"] 
                Returns: ['a', 'b', 'c']

    Extension: Only print the letter if the last letter and first letter are the same
                Returns: ["a"]

"""
# words = ["apple", "banana", "cherry", "ambarella"]
# fl = []
# for element in words:
#     # print(element[0])
#     fl.append(element[0])
# print(fl)
#
# fl = [i[0] for i in words]
# print(fl)
#
# fl_ll = [i for i in words if i[0] == i[-1]]
# print(fl_ll)

###########################################################
"""
Use list comprehension to create a list of 5 tuples where the first element n each tuple is the integers 1 to 5 
and the second element is it square number - for example:
    [(1,1), (2,4), (3,9)....]
"""
t_list = []
for i in range(1,6):
    t = (i, i**2)
    t_list.append(t)
print(t_list)

t_list = [(i, i**2) for i in range(1,600)]
print(t_list)