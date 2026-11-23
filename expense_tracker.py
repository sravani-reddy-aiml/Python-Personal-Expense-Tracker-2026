 # Personal Expense Tracker

expenses = []

while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append([name, amount])
        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\nYour Expenses:")
            for item in expenses:
                print(item[0], "-", item[1])

    elif choice == "3":
        total = 0
        for item in expenses:
            total += item[1]

        print("Total Expenses:", total)

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")
            
