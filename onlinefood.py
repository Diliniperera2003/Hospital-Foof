from abc import ABC, abstractmethod

class FoodOrder(ABC):

    def __init__(self, customer, item_price, distance):
        self.customer = customer
        self._item_price = item_price
        self._distance = distance
        self._paid = 0

    def place_order(self):
        print("Order placed by", self.customer)

    @abstractmethod
    def calculate_total(self):
        pass

    def make_payment(self, amount):
        if amount > 0:
            self._paid += amount
            print("Payment successful:", amount)
        else:
            print("Invalid payment")

    def summary(self):
        print("Customer:", self.customer)
        print("Total Amount:", self.calculate_total())
        print("Amount Paid:", self._paid)

class RestaurantOrder(FoodOrder):

    def calculate_total(self):
        delivery_fee = self._distance * 100
        service_charge = 500

        return self._item_price + delivery_fee + service_charge

class GroceryOrder(FoodOrder):

    def calculate_total(self):
        delivery_fee = self._distance * 80
        packaging_fee = 300

        return self._item_price + delivery_fee + packaging_fee

class BakeryOrder(FoodOrder):

    def calculate_total(self):
        delivery_fee = self._distance * 70
        packaging_fee = 200

        return self._item_price + delivery_fee + packaging_fee

orders = [

    RestaurantOrder("Kamal", 3000, 5),

    GroceryOrder("Nimal", 5000, 4),

    BakeryOrder("Amal", 2500, 3)
]

for order in orders:

    print("\n--------------------------")

    order.place_order()

    total = order.calculate_total()

    order.make_payment(total)

    order.summary()
