# class Kalkulator:
#     def tambah(self,*args):
#         if len(args) == 2:
#             return args[0] + args[1]
#         elif len(args) == 3:
#             return args[0] + args[1] + args[2]
#         else:
#             raise ValueError("Fungsi tambah hanya mendukung 2 atau 3 argumen")

# kalkulator = Kalkulator()
# print(kalkulator.tambah(5,10))
# print(kalkulator.tambah(5,10,15))

# class Kalkulator:
#     def tambah(self, n=3):
#         if n <= 3:
#             print(f"ada {n} pesanan masuk")
#         else:
#             print(f"ada banyak pesanan masuk")

# kalkulator = Kalkulator()
# kalkulator.tambah(2)
# kalkulator.tambah(10)

from multipledispatch import dispatch

class Area:
    @dispatch(int)
    def hitung(self,sisi):
        return sisi * sisi

    @dispatch(int,int)
    def hitung(self,panjang,lebar):
        return panjang * lebar

    @dispatch(int)
    def sapa(self,nama,umur):
        return f"Halo {nama},umur kamu sisa {umur} tahun!"

    @dispatch(int,int)
    def sapa(self,nama,umur):
        return f"Halo {nama},umur kamu sisa {umur} tahun!"

area = Area()
print(area.hitung(5))
print(area.hitung(5,10))
print(area.sapa())
print(area.sapa())