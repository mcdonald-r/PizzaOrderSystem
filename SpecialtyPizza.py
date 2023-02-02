#SpecialtyPizza.py

from Pizza import Pizza

class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        self.size = size
        self.name = name
        if self.size == "S":
            self.price = 12.00 
        elif self.size == "M":
            self.price = 14.00 
        else:
            self.price = 16.00

    def getPizzaDetails(self):
        finalPrice = f'{self.price:.2f}'
        return "SPECIALTY PIZZA\n" + "Size: {}\n".format(self.size) + "Name: {}\n".format(self.name) + "Price: ${}\n".format(finalPrice)
