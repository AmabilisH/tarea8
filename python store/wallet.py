class Wallet:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return f"{self.owner.name}'s wallet balance: {self.balance}"
