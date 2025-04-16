# TODO: Import Budget and Transaction classes
from budget import Budget
from transaction import Transaction

def main():
    budget = Budget()
    #budget.load_from_file("budget_data.txt")

    while True:
        print("\n1. Add Transaction\n2. View Summary\n3. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # TODO: Get input and create Transaction
            description = input("Enter Transaction Desc: ")
            amount = int(input("Enter transaction amount: "))
            category = input("Enter transaction category: ")
            is_income = input("Is this an Income or Expense transaction ? Y(Income) | N(Expense): ")

            if is_income == "Y":
                is_income = True
            else:
                is_income = False

            transaction = Transaction(
                description,
                amount,
                category,
                is_income,
            )

            # TODO: Add transaction to budget
            budget.add_transaction(transaction)

        elif choice == "2":
            # TODO: Print each transaction
            # transactions = budget.transactions
            # for transaction in transactions:
            #     print(transaction)
            transactions = budget.transactions
            for transaction in transactions:
                print(transaction)

            # TODO: Print current balance
            print(f"Balance: £{budget.get_balance()}")

        elif choice == "3":
            budget.save_to_file("budget_data.txt")
            print("Saved! Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
