def is_palindrome(text):
    text = text.lower()  # Mengubah semua huruf menjadi lowercase untuk memastikan perbandingan tidak case-sensitive.
    # Base case
    # Jika panjang string adalah 0 atau 1, maka otomatis dianggap palindrome.
    if len(text) <= 1:
        return True
    # Recursive case
    # Bandingkan karakter pertama (text[0]) dengan karakter terakhir (text[-1]).
    if text[0] == text[-1]:
        # Jika sama, panggil fungsi lagi dengan memotong huruf pertama dan terakhir (slicing)
        # Hal ini terus dilakukan hingga mencapai base case.
        return is_palindrome(text[1:-1])
    else:
        # Jika ada satu saja pasangan huruf yang tidak sama, maka bukan palindrome.
        return False
# Uji Coba Program
print(is_palindrome("Apa")) 
print(is_palindrome("Jokowi"))