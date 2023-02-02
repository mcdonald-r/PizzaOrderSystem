#PizzaOrder.py

class PizzaOrder():
    def __init__(self, time):
        self.time = time
        self.pizzas = []

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        pstr = ""
        total = 0.0

        for pizza in self.pizzas:
            pstr += pizza.getPizzaDetails() + "\n" + "----\n"
            total += pizza.getPrice()

        finalTotal = f'{total:.2f}'

        return "******\n" + "Order Time: {}\n".format(self.time) + pstr + "TOTAL ORDER PRICE: ${}\n".format(finalTotal) + "******\n"
