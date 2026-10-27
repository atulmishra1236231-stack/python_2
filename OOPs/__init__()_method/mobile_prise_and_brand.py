class mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_detail(self):
        print(f"Brand : {self.brand}")
        print(f"Price : {self.price}")

mobile1 = mobile("realme", 10000)
mobile1.show_detail()

