"""
Given a list of n elements in which m elements are unique and n > m,

    1) print a dictionary that represents each element as the key and its occurence as a value
        - each element should appear only one time in the dictionary.

    2) Print which key appears the most times or NONE if there is a tie

    Example:
        lst = ['red', 'yellow', 'red', 'red', 'green', 'yellow']

    The output would be:
        {'red' : 3, 'yellow' : 2, 'green' : 1}
        red
"""
lst = ['red', 'yellow', 'red', 'red', 'green', 'yellow', 'yellow', 'red', 'blue']

print(lst.count('red'))
