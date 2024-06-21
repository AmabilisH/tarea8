from wallet import Wallet
from cart import Cart
from user import User

class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.wallet = Wallet(self)
        self.cart = Cart(self)
        self.items_owned = []  # Lista para almacenar los ítems comprados

    def show_items(self):
        if self.items_owned:
            for item in self.items_owned:
                print(item)
        else:
            print(f"No items owned by {self.name}.")
