"""
Collatz Conjecture Assignment

The Collatz Conjecture is an unsolved mathematical problem that involves
a simple process applied to a positive integer:

    - Start with any positive integer n.
    - If n is even, divide it by 2.
    - If n is odd, multiply it by 3 and add 1.
    - Repeat this process with the new value of n.

The conjecture states that no matter what positive integer you start with,
the sequence will always eventually reach 1.

    Example:
        Start with n = 26.
        If you follow the rules, the sequence generated would be:
            26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1

In this assignment, you will complete the following tasks:

    1) Generate a Collatz sequence for a given starting number.
       Write a function that returns a list of Collatz values starting
       from n and ending when the sequence reaches 1 (inclusive).

       Example input:
       n = 26

       Example output:
       [26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


    2) Create a dictionary of Collatz sequences for a range of values.
       Write a function that returns a dictionary containing the Collatz
       sequences for all starting values within a given range.

           - The keys should be the starting integers.
           - The values should be the corresponding lists of Collatz values.

           Example input:
           start = 3
           end = 6

           Example output:
           {
               3: [3, 10, 5, 16, 8, 4, 2, 1],
               4: [4, 2, 1],
               5: [5, 16, 8, 4, 2, 1],
               6: [6, 3, 10, 5, 16, 8, 4, 2, 1]
           }

"""