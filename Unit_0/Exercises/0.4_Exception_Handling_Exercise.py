"""
Exercise 0.4

Rewrite the Twilzzelrs script from the beginning of this lesson using what you learned about exception handling.

The code from class that needs to be reformatted is shown below

Implement the following:
    1) If the value is valid (integer 0 or greater) add the amount to the count

    2) A ValueError that is raised when someone tries to add a negative amount to their cart with a custom message
        such as "You can't add a negative amount."

    3) A ValueError exception saying something like ‘invalid input’ when a non-integer value is entered.

    4) A generic exception for any other errors saying something “like an unknown error occurred”

    Hint1: Remember try and except have their own block of code
    Hint2: You can capture and display the result of the custom raise message by using the 'as e' keyword

"""

twilzzler_count = 0
add_twizzler  = int(input("How much Twilzzlers would you like to add tp your cart? "))

twilzzler_count += add_twizzler

print(f"You now have {twilzzler_count} Twilzzlers in your cart")