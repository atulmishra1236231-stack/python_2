class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def change_price(self, new_price):
        self.new_price = new_price
        return new_price
        


mobile1 = Mobile("Realme", 10000)

mobile1.change_price(12000)

print(mobile1.new_price)