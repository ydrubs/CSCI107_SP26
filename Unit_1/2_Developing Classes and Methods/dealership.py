"""
This is the code that implements the Car class from the modules:
    1) vehicle 3
    2) vehicle 4
    3) vehicle 5
    4) vehicle 6
"""
# from vehicle3 import Car
#
# car1 = Car('Honda', 'Accord', 'Red', 35000)
# car1.increase_mileage(8) # Use the increase mileage method we wrote with a parameter
# car1.increase_mileage(10)
#
# print(car1.mileage)
# car1.mileage = 0 # Reset mileage for the next part
#
# result = car1.test_drive('ABC6767', 10)
# print(result)
#
# print(car1.number_of_test_drives)

#######################################
# from vehicle4 import Car
#
# not_fusion = Car("Toyota", "Camry", 'red', 35000, 23000)
#
# # print(not_fusion._price) # A notification about accessing a protected class is given
#
# not_fusion._price = 1000 #...HOWEVER ... We can still change the attribute
# # print(not_fusion._price)
#
# not_fusion._price = 35000 # RESET THIS
#
#
# # print(not_fusion.__dealer_price) # ERROR, we cannot access this attribute because the class does not allow it
#
# not_fusion.__dealer_price = 1000 # If we try to change this attribute, Python create a NEW attribute rather than changing the current one
# print(not_fusion.__dealer_price)
#
# # print(dir(not_fusion)) # Notice in the output we NOW have TWO references to dealer_price
#
#
# """<object name>._<Class name>__<Attribute name>"""
# print(not_fusion._Car__dealer_price) # We can access the original attribute by using the name of the class (Car)
#
# print(not_fusion.__dealer_price) # The 'fake' attribute is still part of the object
#
# not_fusion._Car__dealer_price = 20000  # We can change the original attribute by using the class name
# print(not_fusion._Car__dealer_price) # Verify
#
# """
# We can utilize getters and setters to allow a controlled read/write access to protected variables
# This allows to do things like verify conditions before reading and writing
# """
# dealer_price = not_fusion.get_dealer_price()
# print(dealer_price)
#
# not_fusion.set_price(20001) # Change the price of the car
# not_fusion.set_price(5) # Prevents price change and gives message since price < dealer price


###########################################
from vehicle5 import Car

my_car1 = Car('Toyota', 'Camry', 'Red', 35000, 20000)
my_car2 = Car('Ford', 'Fusion', 'Black', 30000, 25000)
# print(my_car1._Car__CAR_COUNT)
# print(my_car2._Car__CAR_COUNT)
# print(Car._Car__CAR_COUNT)


"""
Your try:
    In the vehicle5.py code, write another class method (@classmethod) below the increase_car_count method
    called get_car_count, that provides a way to access the __CAR_COUNT variable without using name mangling
    like we did above.

    Test it out by using it here
"""
# The two are equivalent because a class method has the same effect when called on the class as on an instance
print(my_car2.get_car_count())
print(Car.get_car_count())


"""
Since we used a property decorator for our object, we can now access it like a variable (or attribute) rather then a method
"""
print(my_car1.price) # Check price


my_car1.price = 30000 # Set price
# Reminder - In a previous syntax we had to do this: car1.set_price(35000)
# --- calling methods like defining variables makes using the class much more efficient
# --- This is another example of ENCAPSULATION techniques


