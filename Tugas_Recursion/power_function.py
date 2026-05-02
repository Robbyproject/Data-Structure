def power(base, exp):
    # Base Case
    # Segala angka yang dipangkatkan 0 hasilnya adalah 1.
    # Ini adalah kondisi berhenti agar rekursi tidak berjalan selamanya.
    if exp == 0:
        return 1
    # Recursive case
    # Mengalikan base dengan hasil pemanggilan fungsi itu sendiri 
    # namun dengan nilai eksponen yang dikurangi 1 (menuju base case).
    else:
        return base * power(base, exp - 1)
# Uji Coba Program
print(power(2, 2))
print(power(5, 1))