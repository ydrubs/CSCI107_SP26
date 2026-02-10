"""
Valid phone number

Task:
    Write a function called 'is_valid-number' that accepts a string as a parameter and outputs a boolean representing
    if a phone number is valis or not.

        A number is valid if:
            1) it is in the form ###-#### where all are '#' are integers
            2) The first number is not 0
            3) The first three digits are not 555

        Example:
            Valid: 123-4567
        Not Valid: 12-3456
                   123-456a
"""
def is_valid_number(phone_number : str) -> bool:
    phone_number = list(phone_number)
    return phone_number

phone_number = '123-4567'
r = is_valid_number(phone_number)
print(r)