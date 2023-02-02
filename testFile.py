#testFile.py

from CustomPizza import CustomPizza
from Pizza import Pizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder


def test_Pizza():
    p1 = Pizza("S")
    p2 = Pizza("XL")

    assert p1.getSize() == "S"
    assert p1.getPrice() == 0.0
    p1.setPrice(14.99)
    assert p1.getPrice() == 14.99

    assert p2.getSize() == "XL"
    assert p2.getPrice() == 0.0
    p2.setSize("L")
    assert p2.getSize() == "L"

def test_CustomPizza():
    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("mushroom")
    cp1.addTopping("onion")

    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ mushroom\n\
\t+ onion\n\
Price: $15.00\n"

    cp2 = CustomPizza("S")
    
    assert cp2.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n"

    cp3 = CustomPizza("M")
    cp3.addTopping("pineapple")

    assert cp3.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ pineapple\n\
Price: $10.75\n"

def test_SpecialtyPizza():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"

def test_PizzaOrder():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"

def test_OrderQueue():
    cp1 = CustomPizza("M")
    cp1.addTopping("extra cheese")
    sp1 = SpecialtyPizza("L", "Meat Lovers")
    order = PizzaOrder(174500) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
"******\n\
Order Time: 174500\n\
CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ extra cheese\n\
Price: $10.75\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: L\n\
Name: Meat Lovers\n\
Price: $16.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $26.75\n\
******\n"
