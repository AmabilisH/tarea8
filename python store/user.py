from wallet import Wallet
from ownable import Ownable
from item_manager import show_items, items_list, pick_items, show_items

class User:
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet(self)