from abc import ABC, abstractmethod

class AbstractCalculator(ABC):
    @abstractmethod
    def tambah(self, x, y):
        pass
    @abstractmethod
    def kurang(self, x, y):
        pass
    @abstractmethod
    def kali(self, x, y):
        pass
    @abstractmethod
    def bagi(self, x, y):
        pass

class CalculatorString(AbstractCalculator):
    def tambah(self, x, y):
        return x + y
    def kurang(self, x, y):
        return x - y
    def kali(self, x, y):
        return x * y
    def bagi(self, x, y): 
        return x / y if y != 0 else "Tidak Bisa Dibagi nol"