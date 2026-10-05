order_amount = float(input("Enter order amount (TRY): "))
available_stock = int(input("Enter available stock: "))
requested_quantity = int(input("Enter requested quantity: "))
is_member = input("Is the customer a member? (yes/no): ").strip().lower() == "yes"

if requested_quantity <= 0:
    print("Order Rejected: Requested quantity must be greater than zero.")
elif requested_quantity > available_stock:
    print(f"Order Rejected: Insufficient stock (Available: {available_stock}, Requested: {requested_quantity}).")
else:
    if is_member and order_amount >= 500:
        final_price = order_amount * 0.90
        print("Order Approved: Stock is sufficient. 10% member discount applied!")
    else:
        final_price = order_amount
        print("Order Approved: Stock is sufficient. Standard price applied.")
    
    print(f"Final Price: {final_price:.2f} TRY")
