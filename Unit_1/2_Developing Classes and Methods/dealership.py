"""
This is the code that implements the Car class from the modules:
    1) vehicle 3
    2) vehicle 4
    3) vehicle 5
    4) vehicle 6
"""
from vehicle3 import Car

car1 = Car('Honda', 'Accord', 'Red', 35000)
car1.increase_mileage(8) # Use the increase mileage method we wrote with a parameter
car1.increase_mileage(10)

print(car1.mileage)
car1.mileage = 0 # Reset mileage for the next part

result = car1.test_drive('ABC6767', 10)
print(result)

print(car1.number_of_test_drives)

#######################################


pass # A notification about accessing a protected class is given

pass #...HOWEVER ... We can still change the attribute

pass # RESET THIS


pass # ERROR, we cannot access this attribute because the class does not allow it

# If we try to change this attribute, Python create a NEW attribute rather than changing the current one


pass # Notice in the output we NOW have TWO references to dealer_price


pass # We can access the original attribute by using the name of the class (Car)
pass # The 'fake' attribute is still part of the object

pass  # We can change the original attribute by using the class name
pass # Verify

"""
We can utilize getters and setters to allow a controlled read/write access to protected variables
This allows to do things like verify conditions before reading and writing
"""


pass # Change the price of the car
pass # Prevents price change and gives message since price < dealer price


###########################################



"""
Your try:
    In the vehicle5.py code, write another class method (@classmethod) below the increase_car_count method
    called get_car_count, that provides a way to access the __CAR_COUNT variable without using name mangling
    like we did above.

    Test it out by using it here
"""

# The two are equivalent because a class method has the same effect when called on the class as on an instance



"""
Since we used a property decorator for our object, we can now access it like a variable (or attribute) rather then a method
"""
pass # Check price
pass # Set price
# Reminder - In a previous syntax we had to do this: car1.set_price(35000)
# --- calling methods like defining variables makes using the class much more efficient
# --- This is another example of ENCAPSULATION techniques


