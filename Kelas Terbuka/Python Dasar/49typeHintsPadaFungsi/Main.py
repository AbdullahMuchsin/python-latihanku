## BELAJAR TYPE HINTS PADA FUNGSI

import string


def fungsi_int(nilai:float) -> int: # Menggunkan type hints
    hasil = nilai // 2
    return hasil

HASIL = fungsi_int(29) # Fungsi type hints memberi tahu hasil fungsi/method
print(HASIL)

def huruf_string(kalimat:string) -> string:
    print(kalimat)
    
KALIMAT = huruf_string("Ini Contoh dari Type Hints".upper()) # Jika tidak ada return maka akan noun

