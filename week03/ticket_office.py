tickets_sold = 0
total_revenue = 0.0
free_tickets = 0

while True:
    name = input("Customer name (or q to quit): ").strip()
    if name.lower() == "q":
        break

    age = int(input("Age: "))
    if age < 0 or age > 120:
        print("Invalid age.")
        continue

    day = input("Day (weekday/weekend): ").strip().lower()
    if day not in ["weekday", "weekend"]:
        print("Invalid day.")
        continue

    student_input = input("Student (yes/no): ").strip().lower()
    if student_input not in ["yes", "no"]:
        print("Please answer yes or no.")
        continue

    is_student = (student_input == "yes")

    base_price = 200.0 if day == "weekday" else 250.0

    if age < 6:
        category = "Free"
        price = 0.0
    elif age >= 65:
        category = "Senior"
        price = base_price * 0.50
    elif age <= 12:
        category = "Child"
        price = base_price * 0.60
    elif is_student and age <= 25:
        category = "Student"
        price = base_price * 0.70
    else:
        category = "Standard"
        price = base_price

    print(f"{name}: {price:.2f} TRY ({category})")

    tickets_sold += 1
    total_revenue += price
    if category == "Free":
        free_tickets += 1

if tickets_sold == 0:
    print("No tickets sold.")
else:
    avg_price = total_revenue / tickets_sold
    print(f"Tickets sold: {tickets_sold}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {avg_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")
