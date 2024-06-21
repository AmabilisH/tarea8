from user import User
from ownable import Ownable
from wallet import Wallet  # Asegúrate de importar la clase Wallet

class Seller(User):
    def __init__(self, name):
        super().__init__(name)
        self.items_for_sale = []  # Lista para almacenar los ítems disponibles para la venta
        self.wallet = Wallet(self)
    
    def add_item_for_sale(self, item):
        item.number = len(self.items_for_sale) + 1  # Asigna un número único al ítem
        self.items_for_sale.append(item)
    
    def show_items(self):
        # Mostrar los ítems disponibles para la venta por este vendedor
        if self.items_for_sale:
            print("📜 Items available for sale:")
            for item in self.items_for_sale:
                print(f"{item.number}. {item.name} - Price: {item.price}")
        else:
            print("🚫 No items available for sale.")
    
    def pick_items(self, number, quantity):
        # Seleccionar los ítems basados en el número y la cantidad
        selected_items = []
        for item in self.items_for_sale:
            if item.number == number:
                selected_items.extend([item] * quantity)
        return selected_items