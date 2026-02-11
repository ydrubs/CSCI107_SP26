"""
Lesson 0.4 - Exception Handling

Powerpoint Lesson: 0.4 - Exception Handling
"""

## Slide 1 ##
"""
If we don't handle exceptions, we can't ensure our program will NOT break
    Here, we expect the user to enter an integer number. If they enter a different data type, the program will stop running. 
"""
# twizzler_count = 0
# add_twizzler = int(input("How many twizzlers would you like to add: "))
#
# twizzler_count += add_twizzler
# print(f"You now have {twizzler_count} twizzlers!")


## Slide 4 ##
"""
Syntax errors need to be debugged by the programmer because they cannot be caught at run-time
"""
# print("this is valid")
# print "hello"


"""
Run-time errors CAN be caught during program execution and are usually referred to by a specific name:
"""
# print("hello")
# x = 10/0


## Slide 7 ##
"""
The general syntax for catching exceptions
"""
# try:
#     result = 10/0 # Code that might raise an exception  (but runs if there is no exception)
# #
# except Exception:
#     print("Booo can't divide by zero") # Code to handle the specific exception if it arises
#
# print("other stuff that runs")

## Slide 8 ##
"""
We can keep the program from crashing if a file referenced cannot be found.
"""
# try:
#     with open("nonexistent_file.txt", "r") as file:
#         content = file.read()
#         print(content)
#
# except Exception:
#     print("Error: The file was not found. Please check the file name and try again.")

## Slide 9 ##
"""
A very common exception is an IndexError
"""
# lst = [1,2,3,4]
# # print(lst[4]) # This will cause IndexError use try/except to catch it
#
# try:
#     print(lst[5])
# except Exception:
#     print(f"The index does not exist, the highest index is: {len(lst)-1}")


## Slide 10 ##
"""
Multiple exceptions can occur during run time. We may want to handle each, based on WHAT the exception is.
    The 'Exception' command often is too general to allow us to handle unique exceptions.
    Here, we can get a type error from the user putting in a float OR a division by zero error if zero is entered.
        We would like to handle each differently.
"""
# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
#
# except Exception:
#     print("An error occurred!")  # Not specific; hard to debug



## Slide 11 ##
""""
Here, we handle each type of exception differently. 
"""
# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
#
# except ZeroDivisionError:
#     print("Can't do that, you silly person.")
#
# except ValueError:
#     print("This is not a valid integer, you silly person")
#
# except Exception:
#     print("Something crazy happened, you silly person.")

## Slide 12 ##
"""
The 'raise <type>' command can be used to throw custom exceptions.
This is useful when the program would otherwise interpret a command as valid but it must be handled as an error. 
"""
secret_code = 'secret'
entered_code = input("Please enter the secret code: ")

# pass


## Slide 13 ##
"""
The 'raise' keyword looks for an 'except' keyword that tells it how the error should be handled.
    Here, if an error occurs the 'except' is automatically triggered to handle the exception.
        Since the only way to handle ValueError is to print 'InvalidInput' that is what's displayed regardless of the error.
"""
# age = input("Enter your age: ")
#
# try:
#     if int(age) < 18:
#         raise ValueError ("you are not old enough")
#
#     print("Age confirmed")
#
# except ValueError:
#     print(f"Invalid input")


## Slide 14 ##
"""
Here, after checking user input, if the user:
    1) enters an invalid data type
        - The conditional is skipped (since we don't have an int to check it against)
        - The 'except' is triggered where the error raised by the invalid input is stored to the variable 'e'
        - Invalid Input is printed with the text corresponding to the invalid data type
    2) Enter a number less then 18
        - The conditional triggers
        - The 'except' triggers to handle the error and the text of the 'raise' is stored to the variable 'e'
        - Invalid input is displayed with the text from the raise command ('you are not old enough')
"""
# age = input("Enter your age: ")
#
# try:
#     if int(age) < 18:
#         raise ValueError ("you are not old enough")
#
#     print("Age confirmed")
#
# except ValueError as e:
#     print(f"Invalid input: {e}")
#
#
#
#

