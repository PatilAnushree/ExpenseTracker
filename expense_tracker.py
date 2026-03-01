class ExpenseTracker:

    def __init__(self):
        self.file = "expenses.txt"

    def add_expense(self):
        try:
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")

            with open(self.file, "a") as f:
                f.write(f"{amount},{category}\n")

            print("Expense added successfully")

        except:
            print("Invalid input")

    def view_expenses(self):
        try:
            with open(self.file, "r") as f:
                data = f.readlines()

                if not data:
                    print("No expenses found")
                    return

                print("\nAmount   Category")
                for line in data:
                    amount, category = line.strip().split(",")
                    print(amount, "   ", category)

        except FileNotFoundError:
            print("No expense file found")

    def total_expense(self):
        total = 0
        try:
            with open(self.file, "r") as f:
                for line in f:
                    amount, category = line.strip().split(",")
                    total += float(amount)

            print("Total Expense =", total)

        except:
            print("No data available")

    def category_summary(self):
        summary = {}

        try:
            with open(self.file, "r") as f:
                for line in f:
                    amount, category = line.strip().split(",")
                    summary[category] = summary.get(category, 0) + float(amount)

            for cat, amt in summary.items():
                print(cat, ":", amt)

        except:
            print("No data available")


tracker = ExpenseTracker()

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        tracker.add_expense()
    elif choice == "2":
        tracker.view_expenses()
    elif choice == "3":
        tracker.total_expense()
    elif choice == "4":
        tracker.category_summary()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
