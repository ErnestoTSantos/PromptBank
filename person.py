from datetime import datetime

from count import Checking_account, Legal_account, Savings_account

class Person:

    def __init__(self, name, date):
        self._name = name
        self._date = date

    @property
    def name(self):
        return self._name

    
    @property
    def date(self):
        return self._date

    @name.setter
    def name(self, name:str): 
        if self._name != name and name >= 3:
            self._name = name

    @date.setter
    def date(self, date):
        try:
            if datetime.strptime(date, "%d/%m/%Y"):
                self._date = date
        except:
            self._date = "Undefined"
    
    def age(self):
        date = datetime.today()
        date_person = self.date

        year_now = date.year
        month_now = date.month
        day_now = date.day

        year_person = int(date_person[6:10])
        month_person = int(date_person[3:5])
        day_person = int(date_person[0:2])

        if month_now > month_person:
            return year_now - year_person
        elif month_now == month_person:
            if day_now >= day_person:
                return year_now - year_person
            elif day_now < day_person:
                return (year_now - year_person) - 1
        elif month_now < month_person:
            return (year_now - year_person) - 1                     


class Physique_person(Person):

    def __init__(self, name, date, cpf, count):
        super().__init__(name, date)
        self._cpf = cpf
        self._count = count

    def __str__(self):
        return f"Nome: {self.name}, Idade: {self.age}, Aniversário: {self.birthday}"

    @property
    def count(self):
        return self._count

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        if cpf == 14:
            self._cpf = cpf
        else:
            self._cpf = "Undefined"

    @count.setter
    def count(self, count):
        if isinstance(count, Checking_account) or isinstance(count, Savings_account):
            self._count = count
        else:
            self._count = "Undefined"

class Legal_person(Person):

    def __init__(self, name, date, cnpj, indentification_number, count):
        super().__init__(name, date)
        self._cnpj = cnpj
        self._indentification_number = indentification_number
        self._count = count

    def __str__(self):
        return f"Nome: {self.name}, Idade: {self.age}, Numero de identificação: {self.registration}"

    @property
    def count(self):
        return self._count

    @property
    def indentification_number(self):
        return self._indentification_number

    @property
    def cnpj(self):
        return self._cnpj
    
    @indentification_number.setter
    def indentification_number(self, indentification):
        if indentification != self._indentification_number and indentification.lenght == 14:
            self._indentification_number = indentification
        else:
            self._indentification_number = "Undefined"

    @count.setter
    def count(self, count):
        if isinstance(count, Legal_account):
            self._count = count
        else:
            self._count = "Undefined"

    @cnpj.setter
    def cnpj(self, cnpj):
        if cnpj == 18 and cnpj != self._cnpj:
            self._cnpj = cnpj
        else:
            self._cnpj = "Undefined"
