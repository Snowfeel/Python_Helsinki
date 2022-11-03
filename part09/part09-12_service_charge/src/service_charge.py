# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self,name:str,acc:str,balance:float):
        self.__name = name
        self.__acc = acc
        self.__balance = balance

    def deposit(self,amount: float):
        if amount > 0:
            self.__balance += amount
            self.__service_charge()

    def withdraw(self,amount: float):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__service_charge()

    def __service_charge(self):
        self.__balance -= self.__balance/100
    
    @property
    def balance(self):
        return self.__balance