while True:
    starting_balance = float(input("Enter starting balance: "))
    if starting_balance >= 0:
        break
    print("Starting balance cannot be negative.")

while True:
    deposit = float(input("Enter monthly deposit: "))
    if deposit > 0:
        break
    print("Deposit must be greater than zero.")

while True:
    rate = float(input("Enter monthly interest rate (%): "))
    if rate >= 0:
        break
    print("Interest rate cannot be negative.")

while True:
    goal = float(input("Enter savings goal: "))
    if goal > 0:
        break
    print("Goal must be greater than zero.")

if starting_balance >= goal:
    print("\nStarting balance already meets the goal!")
    print(f"Final balance: {starting_balance:.2f}")
    print("Total interest earned: 0.00")

else:
    balance = starting_balance
    total_interest = 0.0
    goal_reached = False
    months = 0

    print("\nMonth | Interest | Balance")
    print("--------------------------")

    for month in range(1, 61):
        interest = balance * (rate / 100)
        balance = balance + interest + deposit
        total_interest = total_interest + interest
        months = month

        print(f"{month} | {interest:.2f} | {balance:.2f}")

        if balance >= goal:
            goal_reached = True
            break

    if goal_reached:
        print(f"\nGoal reached in {months} month(s)!")
    else:
        print("\nGoal was not reached within 60 months.")

    print(f"Final balance: {balance:.2f}")
    print(f"Total interest earned: {total_interest:.2f}")
