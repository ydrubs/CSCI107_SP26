"""
In this program we:

Demonstrate how a class is created, attributes defined, and methods declared.

"""
class Car():
    def __init__(self):
        self.make = ""
        self.model = ""
        self.color = ""
        self.vin = 0
        self.price = 0
        self.mpg = 0
        self.year = 0
        self.mileage = 0
        self.sold = False
        self.on_lot = False

    def give_discount(self, percentage):
        pass

    def increase_mileage(self, amount):
        pass

    def sell_car(self, final_price):
        pass

    def test_drive(self, license_number):
        pass

if __name__ == "__main__":
    new_car = Car()
    print(new_car)

    another_car = Car
    print(another_car)

    print(type(new_car))