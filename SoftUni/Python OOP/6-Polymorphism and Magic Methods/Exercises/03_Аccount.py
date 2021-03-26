class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        for transaction in self._transactions:
            yield transaction

    def __getitem__(self, index):
        return self._transactions[index]

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __add__(self, other):
        account = self.make_account(other)
        return account

    def __eq__(self, other):
        return self.balance == other.balance

    def make_account(self, other):
        account = Account(self.owner + '&' + other.owner, self.amount + other.amount)
        account._transactions = self._transactions + other._transactions
        return account

    def add_transaction(self, amount):
        if type(amount) != int:
            raise ValueError('please use int for amount')
        print(self.validate_transaction(self, amount))

    @staticmethod
    def validate_transaction(account, amount_to_add):
        bal = account.balance
        bal += amount_to_add
        if bal < 0:
            raise ValueError('sorry cannot go in debt!')
        account._transactions.append(amount_to_add)
        return f'New balance: {account.balance}'

acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
acc4 = Account('Kur', 110)

print(acc4.amount)
print(acc4.balance)
print(acc3.balance)
print(acc4 == acc3)
