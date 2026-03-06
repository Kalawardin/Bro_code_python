cart_count = int(input("How many items do you have? "))
cart = []

for i in range (cart_count):
    item_name = input("Enter product: ")
    item_price = input("Enter price: ")
    cart.append((item_name,item_price))