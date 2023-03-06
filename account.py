class Account:

    def __init__(self, account_id=0, balance=100.00, annual_interest_rate=0.0):
        self.__account_id = account_id
        self.__balance = balance
        self.__annual_interest_rate = annual_interest_rate

    def get_id(self):
        return self.__account_id

    def get_balance(self):
        return self.__balance

    def get_annual_rate(self):
        return self.__annual_interest_rate

    def set_id(self, account_id):
        self.__account_id = account_id

    def set_balance(self, balance):
        self.__balance = balance

    def set_annual_rate(self, rate):
        self.__annual_interest_rate = rate

    def get_monthly_interest_rate(self):
        return self.__annual_interest_rate / 12

    def get_monthly_interest(self, monthly_rate):
        return self.__balance * (monthly_rate/100)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

