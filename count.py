from abc import ABC, abstractmethod

class Count(ABC):

    def __init__(self, agency, count, balance):
        self._agency = agency
        self._count = count
        self._balance = balance

    def __str__(self):
        return f"Agência: {self._agency}, Conta: {self._count}, Saldo: {self._balance}"

    @property
    def agency(self):
        return self._agency
    
    @property
    def count(self):
        return self._count

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value 

    @count.setter
    def count(self, value):
        if self._count != value and value == 7:
            self._count = value

    @agency.setter
    def agency(self, value):
        if self._agency != value and value == 6:
            self._agency = value       

    def deposit(self, value):
        if value > 0:
            self._balance += value

    @abstractmethod
    def withdraw(self, value): pass

class Savings_account(Count):

    def __init__(self, agency, count, balance):
        super().__init__(agency, count, balance)

    def withdraw(self, value):
        if self._balance < value:
            return "Saldo insuficiente!"
        
        self._balance -= value

class Checking_account(Count):

    def __init__(self, agency, count, balance, limit):
        super().__init__(agency, count, balance)
        self._limit = limit
        self._loan = 0
        self.__value_loan = limit + (limit * 1.5/10)

    @property
    def loan(self):
        return self._loan

    @loan.setter
    def loan(self, value):
        if value <= self.__value_loan and value >= 0:
            self.__value_loan -= value
            self._loan += value
            self._balance += value
            return 
            
        self._loan = 0
        return

    def withdraw(self, value):
        if (self._balance + self._limit) < value:
            return "Saldo insuficiente!"

        self._balance -= value
        return f"O novo saldo é de: {self._balance}"

class Legal_account(Count):

    def __init__(self, agency, count, balance, limit):
        super().__init__(agency, count, balance)
        self._limit = limit
        self._investment = None
        self._loan = 0
        self.__value_loan = limit + (limit * 3/10)

    @property
    def loan(self):
        return self._loan

    @property
    def investment(self):
        return self._investment

    @loan.setter
    def loan(self, value):
        if value <= self.__value_loan and value > 0:
            self.__value_loan -= value
            self._loan += value
            self._balance += value
            return
        
        self._loan += 0
        return

    @investment.setter
    def investment(self, value):
        if value <= (self._balance + self._limit) and value > 0:
            value += (value * 5/100)
            self._investment = value
        else:
            self._investment = "Undefined"

    def withdraw(self, value):
        if value > (self._balance + self._limit):
            return "Saldo insuficiente!"

        self._balance -= value
        return f"O novo saldo é de: {self._balance}"