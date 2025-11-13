# Exercise 10: OOP – Encapsulation and Methods

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # private attribute

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Enter a positive amount.")

    # Withdrawal method
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Enter a positive amount.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    # Balance enquiry
    def check_balance(self):
        print(f"Current balance: {self.__balance}")


account = BankAccount(500)
account.deposit(200)
account.withdraw(100)
account.check_balance()
