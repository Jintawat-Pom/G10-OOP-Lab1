class Water:
    def __init__(self,price):
        self.name = 'water'
        self.price = price

class Coffee:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Fruit_Juice:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Milk:
    def __init__(self,price):
        self.name = 'milk'
        self.price = price

class Alcoholic_Beverages:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Cake:
    def __init__(self, name, price, quality):
        self.name = name
        self.price = price
        self.quality = quality

class Pie:
    def __init__(self, name, price, quality):
        self.flavor = name
        self.price = price
        self.quality = quality

class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class Employee:
    def __init__(self, name, age, address, id):
        self.name = name
        self.age = age
        self.address = address
        self.employee_ID = id

class Manager:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

latte = Coffee('Latte',60)
latte.price = 55

shotcake = Cake('shotcake',80,'A')
shotcake.quality = 'C'

Chanakan = Manager('Chanakan',21,'KMITL')
Chanakan.age = 22

mineral_water = Water('Mineral_water',25)
mineral_water.price = 30

orange_juice = Fruit_Juice('Orange juice',40)
orange_juice.name = 'Apple juice'

milk = Milk(20)
milk.price = 25

regency = Alcoholic_Beverages('Regency',285)
regency.price = 275

vanila_cake = Cake('Vanila Cake',99,'A')
vanila_cake.price = 129

chicken_pie = Pie('Chicken Pie',59,'A')
chicken_pie.name = 'Red Been Pie'
chicken_pie.price = 39

customer1 = Customer('Harry',25,'Hogwarts')
customer1.name = 'Ron Weasley'

employee1 = Employee('Emma',29,'KMITL','1')
employee1.age = 28