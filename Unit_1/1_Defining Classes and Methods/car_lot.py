# import vehicle1 # Import the Car class from the vehicle1 module
# from vehicle1 import Car
#
# new_car = Car() # Create an instance of the car class as an object which we call 'my_car'
# print(new_car) # This returns the memory reference of the object created (we will look at making this more informative later)
#
# print(new_car.make)
# new_car.make = 'Ford' # Set the 'make' attribute of the car
# print(new_car.make)
#
# new_car.model = "Fusion" # Set the 'model' attribute of the car
# print(new_car.model)
# print(f"Thanks for buying the {new_car.make} {new_car.model}")
#
# special_car = new_car.make
# print(special_car)
#
# another_car = Car() # Create another object from the Car() class
# another_car.make = "Lamboghini"
#
# print(new_car.make, another_car.make)
#
# print(dir(new_car))
#
# new_car.price = 45000
# new_car.give_discount(10)

###########################################################
from vehicle2 import Car

# Create an object by passing in attribute to the constructor (__init__)
cool_car = Car("Ford", "Fusion", "Red", 35000)

# We can see documentation for any object (or class) by using help
print(dir(cool_car))
print(help(cool_car))

# Objects have inherent methods that can be accessed and manipulated
# Here, we have the ability to represent the attributes as dictionaries
pass

# Your turn - Add two more car objects by passing in the required parameters
pass

""" 
    We can create objects using a loop as well.
    Here we define the number of objects and create a list to hold them. 
    
    Then we add them using a loop
"""
pass


#Print individual attributes for each car
pass

#We can also apply conditionals to our objects
pass





