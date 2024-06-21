from ownable import Ownable

class Cart(Ownable):
    def __init__(self, owner):
        super().__init__(owner)
        self.items = []

    def add(self, item):
        self.items.append(item)

    def show_items(self):
        if self.items:
            for item in self.items:
                print(item)
        else:
            print("The cart is empty.")

    def total_amount(self):
        return sum(item.price for item in self.items)

    def check_out(self):
        total = self.total_amount()
        if self.owner.wallet.balance >= total:
            for item in self.items:
                self.owner.wallet.balance -= item.price
                item.owner.wallet.balance += item.price
                item.owner = self.owner  # Transfer ownership
                self.owner.items_owned.append(item)  # Add item to customer's owned items
            self.items = []
            print("Purchase completed successfully.")
        else:
            print("Insufficient funds to complete the purchase.")
