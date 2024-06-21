from customer import Customer
from item import Item
from seller import Seller

# Crear un objeto vendedor
seller = Seller("DIC Store")

# Añadir artículos a la venta asociados al vendedor
seller.add_item_for_sale(Item("CPU", 40830, seller))
seller.add_item_for_sale(Item("Memory", 13880, seller))
seller.add_item_for_sale(Item("Motherboard", 28980, seller))
seller.add_item_for_sale(Item("Power Unit", 8980, seller))
seller.add_item_for_sale(Item("PC Case", 8727, seller))
seller.add_item_for_sale(Item("3.5-inch HDD", 10980, seller))
seller.add_item_for_sale(Item("2.5-inch SSD", 13370, seller))
seller.add_item_for_sale(Item("M.2 SSD", 12980, seller))
seller.add_item_for_sale(Item("CPU Cooler", 13400, seller))
seller.add_item_for_sale(Item("Graphics Card", 23800, seller))

print("🤖 Please tell me your name")
customer = Customer(input())

print("🏧 Please input the amount to charge to your wallet")
customer.wallet.deposit(int(input()))

print("🛍️ Starting shopping")
end_shopping = False
while not end_shopping:
    print("📜 Item list")
    seller.show_items()

    print("️️⛏ Please enter the item number")
    number = int(input())

    print("⛏ Please enter the quantity")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Cart contents")
    customer.cart.show_items()
    print(f"🤑 Total amount: {customer.cart.total_amount()}")

    print("😭 End shopping? (yes/no)")
    end_shopping = input() == "yes"

print("💸 Confirm purchase? (yes/no)")
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Results ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️Items owned by {customer.name}")
customer.show_items()
print(f"😱👛 {customer.name}'s wallet balance: {customer.wallet.balance}")

print(f"📦 {seller.name}'s inventory status")
seller.show_items()
print(f"😻👛 {seller.name}'s wallet balance: {seller.wallet.balance}")

print("🛒 Cart contents")
customer.cart.show_items()
print(f"🌚 Total amount: {customer.cart.total_amount()}")

print("🎉 End")
