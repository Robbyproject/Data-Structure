class Hewan:
    def suara(self):
        print("Hewan ini mengeluarkan suara")

class Kucing(Hewan):
    def suara(self):
        print("Meong")

class Anjing(Hewan):
    def suara(self):
        print("Guk guk")

class Buaya(Hewan):
    def suara(self):
        print("Afahiyaa??")

kucing = Kucing()
kucing.suara()

vandy = Buaya()
vandy.suara()