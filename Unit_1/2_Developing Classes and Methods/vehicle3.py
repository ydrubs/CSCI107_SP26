"""
In this program we start to implement the methods of our Car class.

Methods are like functions within a class that allow an object to do an 'action' when called on the object

We will practice passing in arguments into the methods in order to act on the data recieved
"""
class Car():
    def __init__(self, make:str, model, color, price, sold = False):
        self.make = make
        self.model = model
        self.color = color
        self.vin = 0
        self.price = price
        self.mpg = 0
        self.year = 0
        self.mileage = 0
        self.sold = sold
        self.on_lot = False

        self.number_of_test_drives = 0


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

        self.number_of_test_drives +=1

        self.increase_mileage(amount_driven)
        return (f'Thanks for driving the {self.make} {self.model},'
                f'you put on {amount_driven} miles.'
                f'The car now has {self.mileage} miles now.')