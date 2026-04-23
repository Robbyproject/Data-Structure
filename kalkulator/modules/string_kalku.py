from modules.calculator_string import CalculatorString

class Proses:
    def __init__(self):
        self.__satuan = {
            "Nol": 0, "Satu": 1, "Dua": 2, "Tiga": 3, "Empat": 4,
            "Lima": 5, "Enam": 6, "Tujuh": 7, "Delapan": 8, 
            "Sembilan": 9, "Sepuluh": 10, "Sebelas": 11
        }
        self.kalkulator = CalculatorString()

    def hitung_kata(self, kata1, operator, kata2):
        n1 = self.__satuan.get(kata1.capitalize())
        n2 = self.__satuan.get(kata2.capitalize())

        if n1 is None or n2 is None:
            return "Angka kata tidak dikenal."

        if operator == "tambah":
            return self.kalkulator.tambah(n1, n2)
        elif operator == "kurang":
            return self.kalkulator.kurang(n1, n2)
        elif operator == "kali":
            return self.kalkulator.kali(n1, n2)
        elif operator == "bagi":
            return self.kalkulator.bagi(n1, n2)
        else:
            return "Operator tidak dikenal."