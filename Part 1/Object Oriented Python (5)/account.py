class Account:
    def __init__(self):
        self.transactions = []

    def deposit(self, amount):
        transaction = ("deposit", amount)
        self.transactions.append(transaction)

    def withdraw(self, amount):
        transaction = ("withdraw", amount)
        self.transactions.append(transaction)

    def balance(self):
        total = 0
        for kind, amount in self.transactions:
            if kind == "deposit":
                total += amount
            elif kind == "withdraw":
                total -= amount
        return total

    def __repr__(self):
        return"<Account: {}>".format(self.transactions)
