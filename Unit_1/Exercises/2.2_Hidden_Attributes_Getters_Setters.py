"""
2.2 - Hidden Attributes and Getters/Setters

Goal: You will modify your existing class from previous lessons.

STEP-BY-STEP:
    STEP 1 — Add a Protected Attribute
        Choose one attribute that the object should not be changed directly by outside code (but can still be read if needed).
        Add it using one underscore:
            For example:
                self._protected_value = 10

    STEP 2 - Add a Private Attribute
        Choose another attribute that should be fully hidden from users, because it affects internal logic.
            Add it using two underscores:
            For example:
                self.__private_value = 100

    STEP 3 - Write a Getter Method (for one of your protected or private methods)

    STEP 4 - Write a Setter Method and include a validation check before the return (for one of your protected or private methods)

    STEP 5 — Demonstrate Your Getter and Setter Methods

        After you finish the class:
        - Create an object
        - Try printing the protected attribute
        - Use your getter to read the private attribute
        - Use your setter to change the private attribute
        - Print the private value again to confirm it changed
"""