import csv
import json

expenses = []


def generate_id():
    if expenses:
        return max(expense["ID"] for expense in expenses) + 1
    return 1


def get_amount():
    while True:
        try:
            amount = float(input("Enter Amount: ₹"))
            if amount < 0:
                print("Amount cannot be negative.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid amount.")


def add_expense():
    expense = {
        "ID": generate_id(),
        "Date": input("Enter Date (YYYY-MM-DD): "),
        "Category": input("Enter Category: "),
        "Description": input("Enter Description: "),
        "Amount": get_amount(),
        "Payment": input("Enter Payment Method: ")
    }

    expenses.append(expense)
    print("\n✓ Expense added successfully.")


def view_expenses():

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "=" * 90)
    print(f"{'ID':<5}{'Date':<15}{'Category':<15}{'Description':<20}{'Amount':<12}{'Payment'}")
    print("=" * 90)

    for expense in expenses:

        print(
            f"{expense['ID']:<5}"
            f"{expense['Date']:<15}"
            f"{expense['Category']:<15}"
            f"{expense['Description']:<20}"
            f"{expense['Amount']:<12.2f}"
            f"{expense['Payment']}"
        )

def update_expense():

    try:
        expense_id = int(input("Enter Expense ID to update: "))
    except ValueError:
        print("Please enter a valid Expense ID.")
        return

    for expense in expenses:

        if expense["ID"] == expense_id:

            expense["Date"] = input("Enter New Date: ")
            expense["Category"] = input("Enter New Category: ")
            expense["Description"] = input("Enter New Description: ")
            expense["Amount"] = get_amount()
            expense["Payment"] = input("Enter New Payment Method: ")

            print("\n✓ Expense updated successfully.")
            return

    print("\n✗ Expense ID not found.")


def delete_expense():

    expense_id = int(input("Enter Expense ID to delete: "))

    for expense in expenses:

        if expense["ID"] == expense_id:

            expenses.remove(expense)

            print("\n✓ Expense deleted successfully.")
            return

    print("\n✗ Expense ID not found.")

def search_expense():

    keyword = input("Enter Category or Description to search: ").lower()

    found = False

    print("\n" + "=" * 90)
    print(f"{'ID':<5}{'Date':<15}{'Category':<15}{'Description':<20}{'Amount':<12}{'Payment'}")
    print("=" * 90)

    for expense in expenses:

        if (
            keyword in expense["Category"].lower()
            or keyword in expense["Description"].lower()
        ):

            print(
                f"{expense['ID']:<5}"
                f"{expense['Date']:<15}"
                f"{expense['Category']:<15}"
                f"{expense['Description']:<20}"
                f"{expense['Amount']:<12.2f}"
                f"{expense['Payment']}"
            )

            found = True

    if not found:
        print("\nNo matching expenses found.")


def category_summary():

    if not expenses:
        print("\nNo expenses found.")
        return

    summary = {}

    for expense in expenses:

        category = expense["Category"]

        summary[category] = summary.get(category, 0) + expense["Amount"]

    print("\n" + "=" * 40)
    print("CATEGORY SUMMARY")
    print("=" * 40)

    for category, amount in summary.items():
        print(f"{category:<20} ₹{amount:.2f}")


def monthly_summary():

    if not expenses:
        print("\nNo expenses found.")
        return

    summary = {}

    for expense in expenses:

        month = expense["Date"][:7]

        summary[month] = summary.get(month, 0) + expense["Amount"]

    print("\n" + "=" * 40)
    print("MONTHLY SUMMARY")
    print("=" * 40)

    for month, amount in summary.items():
        print(f"{month:<15} ₹{amount:.2f}")


def total_expenses():

    if not expenses:
        print("\nNo expenses found.")
        return

    total = sum(expense["Amount"] for expense in expenses)

    print("\n" + "=" * 40)
    print(f"Total Expenses : ₹{total:.2f}")
    print("=" * 40)


def save_csv():

    with open("expenses.csv", "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "ID",
                "Date",
                "Category",
                "Description",
                "Amount",
                "Payment"
            ]
        )

        writer.writeheader()
        writer.writerows(expenses)

    print("\n✓ Saved to expenses.csv")


def save_json():

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("\n✓ Saved to expenses.json")


def main():

    while True:

        print("\n" + "=" * 45)
        print("        PERSONAL EXPENSE TRACKER")
        print("=" * 45)

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Search Expense")
        print("6. Category Summary")
        print("7. Monthly Summary")
        print("8. Total Expenses")
        print("9. Save to CSV")
        print("10. Save to JSON")
        print("11. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            update_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            search_expense()

        elif choice == "6":
            category_summary()

        elif choice == "7":
            monthly_summary()

        elif choice == "8":
            total_expenses()

        elif choice == "9":
            save_csv()

        elif choice == "10":
            save_json()

        elif choice == "11":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()