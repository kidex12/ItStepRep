class Customer:
    def __init__(self, name):
        self.name = name
    def cart(self, order):
        self.order = order



class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total


    def show_order(self):
        print(self.customer)
        print("Замовлення:")
        for i in self.items:
            print(i.name)
        print(f"Загальна сума: {self.get_total()} грн")



customer1 = Customer("Кирил")
order1 = Order(customer1)

item1 = MenuItem("Борщ", 70)
item2 = MenuItem("Стейк", 100)

order1.add_item(item1)
order1.add_item(item2)

order1.show_order()