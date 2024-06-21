from ownable import Ownable

class Item(Ownable):
    def __init__(self, name, price, seller):
        super().__init__(seller)
        self.name = name
        self.price = price
        self.number = None  # Número del ítem, será asignado por el vendedor

    def __str__(self):
        return f"{self.name} - Price: {self.price}"
