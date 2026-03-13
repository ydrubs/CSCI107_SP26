"""
This program demonstrates inheritance using a base class called Car.
The Car class contains attributes and behaviors that all cars share.

Two child classes inherit from Car:
- GasolineCar
- ElectricCar

These child classes reuse the common functionality of Car and override
the refuel() method to implement behavior specific to each type of car.
"""

class Car():
    __CAR_COUNT = 0# Define a static class method and make it private
    @classmethod
    def increase_car_count(cls): #Increase the car count every time an instance is created
        cls.__CAR_COUNT +=1

    # GET NUMBER OF CARS ON LOT
    @classmethod
    def get_car_count(cls):
        return cls.__CAR_COUNT

    def __init__(self, make, model, color, price, dealer_price, sold = False):
        # Increase count automatically whenever a new instance is created
        Car.increase_car_count()

        self.make = make
        self.model = model
        self.color = color
        self.vin = 0

        # _ suggests that the attribute should not be changes outside of the class but still accessible outside the class in the normal way
        self._price = price

        self.mpg = 0
        self.year = 0
        self.mileage = 0
        self.sold = sold
        self.on_lot = False

        self.number_of_test_drives = 0

        # Makes it so an attribute is harder to access (but not impossible) from outside the class
        self.__dealer_price = dealer_price

    def give_discount(self, percentage):
        """THis is some useful stuff"""
        pass

    def increase_mileage(self, amount):
        self.mileage += amount
        return self.mileage

    def sell_car(self, final_price):
        pass

    def test_drive(self, license_number, amount_driven):
        """
        Tracks the test drives of a car instance
        :param license_number: String
               amount_driven: int
        :return: Drive Receipt: String
        """
        print(f'License plate {license_number} attached')

        self.number_of_test_drives += 1

        self.increase_mileage(amount_driven)
        return (f'Thanks for driving the {self.make} {self.model},'
                f'you put on {amount_driven} miles.'
                f'The car now has {self.mileage} miles now.')

    # def get_dealer_price(self):
    #     return f"The dealer paid ${self.__dealer_price} for the car"

    @property
    def price(self):
        return f"The dealer paid ${self.__dealer_price} for the car"

    @price.setter
    def price(self, price):
        if price > self.__dealer_price:
            self._price = price
            print(f"Setting new price to {self._price}")
            # return self._price

    # def set_price(self, price):
    #     if price > self.__dealer_price:
    #         self._price = price
    #         print(f"Setting new price to {self._price}")
    #         return self._price

        else:
            print(f"You will lose money, don't set this price")

    def refuel(self):
        return "This vehicle needs to be refueled"

class GasolineCar(Car):
    def __init__(self, make, model, color, price, dealer_price, fuel_tank_size, sold = False):
        super().__init__(make, model, color, price, dealer_price, sold)

        self.fuel_tank_size = fuel_tank_size

    def refuel(self, gallons = 0):
        gallons_filled = gallons
        if gallons_filled > self.fuel_tank_size:
            return f"You put in {self.fuel_tank_size} gallons"
        else:
            return f"You added {gallons_filled} of gas"

class ElectricCar(Car):
    def __init__(self, make, model, color, price, dealer_price, battery_range, sold = False):
        super().__init__(make, model, color, price, dealer_price, sold)

        self.battery_range = battery_range

    def refuel(self, charge_time_minutes = 0):
        total_charge_range = 13 * charge_time_minutes
        if total_charge_range >= self.battery_range:
            return f"You added {self.battery_range} miles to your range"
        else:
            return f"You added {total_charge_range} miles to your range, hapy driving!"