"""
In this program we explore how magic methods (or dunder methods) work

    Magic methods in Python are special built-in functions that let your objects behave in 'familiar ways',
        such as being created, printed, or compared without you having to manually write separate code for those behaviors.


    We will take all the code from vehicle6 then implement:
        __str__ and __eq__ magic methods into the Car class

"""
class Car():

    __CAR_COUNT = 0 # Define a static class method and make it private
    @classmethod
    def increase_car_count(cls): #Increase the car count every time an instance is created
        cls.__CAR_COUNT +=1

    def __init__(self, make, model, color, price, dealer_price, sold = False):
        # Increase count automatically whenever a new instance is created
        Car.increase_car_count()


        self.make = make
        self.model = model
        self.color = color
        self.vin = ""
        self.__price = price
        self.mpg = 0
        self.year = 0
        self.mileage = 0
        self.sold = sold
        self.on_lot = False
        self.numb_of_test_drives = 0
        self.__dealer_price = dealer_price

    def give_discount(self, percentage):
        pass

    def increase_mileage(self, amount):
        self.mileage += amount
        return self.mileage

    def sell_car(self, final_price):
        pass

    def test_drive(self, license_number, amount_driven):
        print(f'Licence plate {license_number} attached.')
        self.numb_of_test_drives +=1
        self.increase_mileage(amount_driven)
        return f"Thanks for test driving the {self.make} {self.model}. You put on {amount_driven} during the test-drive." \
               f"This vehicle now has {self.mileage} miles"

    ##getter/setter methods
    # def get_price(self):
    #     return self.__price
    #
    # def set_price(self, price):
    # if price > self.__dealer_price:
    #     print(f"Price set to {price}")
    #     self.__price = price
    # else:
    #     print(f"The price of {price} will result in a loss. Price not set.")

    #Using the propery getter and setter decorators
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > self.__dealer_price:
            print(f"Price set to {price}")
            self.__price = price
        else:
            print(f"The price of {price} will result in a loss. Price not set.")


    def get_dealer_price(self):
        return self.__dealer_price

    """
    Use the __eq__ magic method to define how two objects should be compared for equality, 
    allowing you to customize what it means for two instances of a class to be considered equal.
    """
    def __eq__(self, other):
        if self.price == other.price:
            return True
        else:
            return False

    """
    Use the __str__ magic method to define a human-readable string representation of an object, 
    which is displayed when the object is printed or converted to a string.
    """
    def __str__(self):
        return f'{self.make} {self.model}'

class GasolineCar(Car):

    def __init__(self, make, model, color, price, dealer_price, fuel_tank_size, sold=False):
        super().__init__(make, model, color, price, dealer_price, sold)

        self.fuel_tank_size = fuel_tank_size

    def refuel(self, gallons = 0):
        gallons_filled = gallons
        if gallons_filled > self.fuel_tank_size:
            return f"You filled {self.fuel_tank_size} gallons of gas."
        else:
            return f"You filled {gallons_filled} gallons of gas"

class ElectricCar(Car):

    def __init__(self, make, model, color, price, dealer_price, battery_range, sold=False):
        super().__init__(make, model, color, price, dealer_price, sold)

        self.battery_range = battery_range

    def refuel(self, charge_time_minutes = 0):
        total_charge_range = 13 * charge_time_minutes
        if total_charge_range >= self.battery_range:
            return f"You added {self.battery_range} miles to your battery"
        else:
            return f"You added {total_charge_range} miles to your range"


if __name__ == "__main__":
    car1 = GasolineCar("Hummer", "H3", "Green", 70000, 30000, 40)
    car2 = ElectricCar("Tesla", "Model3", "Red", 42000, 31000, 500)

    print(car1) # Gives a memory reference (without a __str__ method give memory location)
    print(car2) # If we have a __str__ method we can control what the object shows

    print(car1 == car2) # False because cars are not the price
    car1.price = 42000
    print(car1 == car2) # Now True because prices are the same

    print(car1.__eq__(car2)) # Does exactly the same thing
