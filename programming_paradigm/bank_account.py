"""
Objective : Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations. 
Use command line arguments to interact with instances of this class.
"""
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount : float) -> str:
        """Deposit money into the account.
        args:
            amount (float): The amount to deposit.
        returns:
            str: A message indicating the result of the deposit.
        """
        if amount > 0:
            self.balance += amount
            return (f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount: float) -> str:
        """Withdraw money from the account.
        args:
            amount (float): The amount to withdraw.
        returns:
            str: A message indicating the result of the withdrawal.
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return (f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def display_balance(self) -> str:
        """Display the current balance.
        returns:
            str: The current balance.
        """
        return (f"Current balance: ${self.balance:.2f}")