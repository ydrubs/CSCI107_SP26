"""
Exercise 0.2 - List Comprehension Practice

Part 1: Given the following list:

    numbers = [3, 10, 7, 21, 4, 18, 9, 2]

    1) Create a list comprehension that returns only the numbers greater than 8.

        Should return: [10, 21, 18, 9]

    2) Using the filtered list from Exercise 1, write a new list comprehension that returns each number divided by 3.

        Should return: [3.33, 7.0, 6.0, 3.0]

    3) Using the results from Exercise 1 and Exercise 2, create a list comprehension that produces a list of tuples,
        where each tuple contains: (original_number, transformed_number)

        Should return: [(10, 3.33), (21, 7.0), (18, 6.0), (9, 3.0)]
        HINT: (l1[i], l2[i]) will be the output expression that goes into the list comprehension
"""
# SOLUTION HERE


"""
Part 2 (DIFFICULT/ OPTIONAL): Movie data analyzer -
    Given a list of tuples called 'movies' and another list of tuples called 'box office' shown below:

                movies = [
                ("Inception", 2010, 8.8, ["sci-fi", "action"]),
                ("The Lion King", 1994, 8.5, ["animation", "family"]),
                ("Interstellar", 2014, 8.6, ["sci-fi", "drama"]),
                ("The Room", 2003, 3.7, ["drama"]),
                ("Toy Story", 1995, 8.3, ["animation", "comedy"]),
                ("Random B-Movie", 2018, 4.2, ["action", "thriller"]),
            ]

                box_office = [
                    ("Inception", 829),
                    ("The Lion King", 968),
                    ("Interstellar", 677),
                    ("The Room", 1.8),
                    ("Toy Story", 373),
                    ("Random B-Movie", 12)
                ]

    Use list comprehension to do the following:

    1) Hidden Gems of the 2000's - Create a list called 'hidden_gems' that contains tittles of movies that:
        - Were released before 2005 AND
        - have a rating of 7.0 or higher

        HINT: You only need the movies list for this one.

        This should return: ['The Lion King', 'Toy Story']

    2) Bof Office hits - Create a list called 'box_office_hits' that contain movies made AFTER 2005 AND
        have a box office profit above 800.

        Use two list comprehensions to do this (you will use the output of the first as part of the second)

        The output should be: ['Inception']
"""
# SOLUTION HERE