class Employee:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        print(self.name)

class PEmployee:
    def __init__(self,name,age):
        self.name = name
        self._age = age

class PREmployee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
        self.__accountNumber = accountNumber

    def show_salary(self):
        return self.__salary

    def get_salary(self):
        return self.__salary
    def set_salary(self, year):
        if year == 2:
            self.__salary = self.__salary + (self.__salary * 0.1)
        else:
            # self.__salary = self.__salary
            print("Ga naik Gaji")
    
    def show_accountNumber(self):
        return self.__accountNumber

    def get_accountNumber(self):
        return self.__accountNumber

class SubEmployee(PEmployee):
    def show_age(self):
        print(f"age: {self._age}")
        print(f"name: {self._nama}")

pemp = SubEmployee("Joko", 56)
Remp = PREmployee("Miko", 10_000_000)
emp = Employee("Joko")
emp.display_name()

print(pemp._age)
print(emp.name)
print(Remp.show_salary())
parent = PEmployee("Hitler", 105)
print(parent._age)

Remp.set_salary(20)
print(Remp.get_salary())