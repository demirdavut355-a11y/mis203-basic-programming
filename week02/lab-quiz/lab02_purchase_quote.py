item1_name = input("Enter name of item 1: ")
item1_qty = int(input("Enter quantity of item 1: "))
item1_price = float(input("Enter unit price of item 1: "))

item2_name = input("Enter name of item 2: ")
item2_qty = int(input("Enter quantity of item 2: "))
item2_price = float(input("Enter unit price of item 2: "))

delivery_fee = float(input("Enter delivery fee: "))
tax_percent = float(input("Enter tax percentage (e.g. 10): "))

item1_total = item1_qty * item1_price
item2_total = item2_qty * item2_price
subtotal = item1_total + item2_total
tax_amount = subtotal * (tax_percent / 100)
final_total = subtotal + tax_amount + delivery_fee

print("\n" + "=" * 32)
print("         PURCHASE QUOTE")
print("=" * 32)
print(f"{item1_name} ({item1_qty} x {item1_price:.2f}): {item1_total:.2f} TRY")
print(f"{item2_name} ({item2_qty} x {item2_price:.2f}): {item2_total:.2f} TRY")
print("-" * 32)
print(f"Subtotal:         {subtotal:.2f} TRY")
print(f"Tax ({tax_percent:.0f}%):          {tax_amount:.2f} TRY")
print(f"Delivery Fee:     {delivery_fee:.2f} TRY")
print("-" * 32)
print(f"FINAL TOTAL:      {final_total:.2f} TRY")
print("=" * 32)
