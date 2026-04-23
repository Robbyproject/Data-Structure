from modules.string_kalku import Proses

def main():
    p = Proses()
    print("Kalkulator String")
    print("Contoh input: Satu tambah Dua")
    
    while True:
        tanya = input("\nMasukkan operasi (atau 'keluar'): ")
        if tanya.lower() == 'keluar': break
        
        try:
            k1, op, k2 = tanya.split()
            hasil = p.hitung_kata(k1, op, k2)
            print(f"Hasil: {hasil}")
        except ValueError:
            print("Format salah! Gunakan format: [Angka] [Operator] [Angka]")
main()