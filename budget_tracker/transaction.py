class Transaction:
    # TODO: Create the __init__ method with:
    # description (string), amount (float), category (string), is_income (bool)
    def __init__(self, description, amount, category, is_income):
        self.description = description
        self.amount = amount
        self.category = category
        self.is_income = is_income

    # TODO: Create the __str__ method to return a formatted string like:
    # "Income: Freelance Work | $250.00 | Category: Work"
    def __str__(self):
        transaction_type = "Income" if self.is_income else "Expense"
        return f"{transaction_type}: {self.description} | \xA3{self.amount} | Category: {self.category}"
