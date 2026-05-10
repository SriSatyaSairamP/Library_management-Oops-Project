## 09-05-2026

## Bank-Oops-Project

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

    def deposit(self,amount):
        self.__balance+=amount
        print(f"₹{amount} deposited successfully")

    @abstractmethod
    def withdraw(self,amount):
        pass

    def display(self):
        print(f"\nAccount Holder : {self.name}")
        print(f"Balance:₹{self.__balance}")

class SavingsAccount(Account):
    def withdraw(self,amount):

        if amount>self.get_balance():
            print("Insufficient Balance")

        elif amount >40000:
            print("Withdrawal Daily Limit Exceeded")

        else:
            new_balance=self.get_balance()-amount

            self.set_balance(new_balance)
            print(f"₹{amount} withdrawn successfully")

class CurrentAccount(Account):

    def withdraw(self,amount):

        if amount>self.get_balance():
            print("Insufficient Balance")

        else:
            new_balance=self.get_balance() - amount
            self.set_balance(new_balance)

            print(f"₹{amount} withdrawn successfully")

class Bank:
    def __init__(self,total):
        self.total=total

    def __add__(self,other):
        return Bank(self.total+other.total)

    def show_total(self):
        print(f"\nTotal Bank Balance: ₹{self.total}")

acc1 = SavingsAccount("Ish@@n", 20000)
acc2 = CurrentAccount("Sairam", 15000)

acc1.display()
acc1.deposit(5000)
acc1.withdraw(8000)
acc1.display()

acc2.display()
acc2.withdraw(3000)
acc2.display()

bank1 = Bank(acc1.get_balance())
bank2 = Bank(acc2.get_balance())
bank3 = bank1 + bank2
bank3.show_total()