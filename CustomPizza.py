#CustomPizza.py

from Pizza import Pizza

class CustomPizza(Pizza):
    def __init__(self, size):
        self.size = size
        self.toppings = []

        if self.size == "S":
            self.price = 8.00
        elif self.size == "M":
            self.price = 10.00
        else:
            self.price = 12.00

    def addTopping(self, topping):
        self.toppings.append("\t+ {}\n".format(topping))

        if self.size == "S":
            self.price += 0.50
        elif self.size == "M":
            self.price += 0.75
        else:
            self.price += 1.00
    
    def getPizzaDetails(self):
        topStr = ""

        for top in self.toppings:
            topStr += top

        finalPrice = f'{self.price:.2f}'

        return "CUSTOM PIZZA\n" + "Size: {}\n".format(self.size) + "Toppings:\n" + topStr + "Price: ${}\n".format(finalPrice)
