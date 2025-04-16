# TODO: Import Transaction class from transaction.py
from transaction import Transaction

class Budget:
    def __init__(self):
        # TODO: Create a list to store transactions
        self.transactions = []
        # [Transaction("ads", 500, "work", True), Transaction("ads", 500, "work", True)]

    def add_transaction(self, transaction):
        # TODO: Append the transaction to the list
        self.transactions.append(transaction)

    def get_balance(self):
        # TODO: Loop through transactions and calculate the balance
        balance = 0
        for transaction in self.transactions: 
            if transaction.is_income:  
                balance += transaction.amount
            else:
                balance -= transaction.amount
        return balance

    def save_to_file(self, filename):
        # TODO: Write transactions to a file
        with open(filename, 'w') as file:
            for transaction in self.transactions:
                file.write(str(transaction))
                file.write("\n")

    def load_from_file(self, filename):
        # TODO: Read file and load transactions using Transaction class
        with open(filename, "r") as file:
            transactions_with_newline = file.readlines()
            for transaction in transactions_with_newline:
                # 'Income: Freelance | £500 | Category: Work '
                transaction_without_newline = transaction[:-1]

                # ["Income: Freelance ", " �500 ", " Category: Work"]
                transaction_bits = transaction_without_newline.split("|")

                is_income_and_description = transaction_bits[0].strip()
                amount = transaction_bits[1].strip()
                category = transaction_bits[2].strip()

                # Get is_income and description details from "Income: Freelance"
                is_income, description = is_income_and_description.split(":")
                is_income = True if is_income == "Income" else False
                description = description.strip()

                # Get the amount details from "�500"
                amount = int(amount[1:])

                # Get the category details from "Category: Work"
                category = category.split(":")[1].strip()

                transaction = Transaction(description, amount, category, is_income)

                self.transactions.append(transaction)
