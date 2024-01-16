class BankAccount:
    total_accounts = 0


    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    def show_balance(self):
        return self.balance

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @staticmethod
    def validate_amount(balance):
        return balance >= 0


mantrenas_lapinenas = BankAccount("Mantrenas", 745.65)
vilkas_papjauskas = BankAccount("Vilkas", 1472.95)

print(mantrenas_lapinenas.show_balance())
print(vilkas_papjauskas.show_balance())

print(mantrenas_lapinenas.validate_amount(10))
print(vilkas_papjauskas.validate_amount(-10))

print("Total_accounts:", BankAccount.get_total_accounts())