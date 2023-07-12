# BELAJAR DEFAULT ARGUMENT

# Contoh 1
def fungsi1(angka = "Tidak ada angka yang di tambahkan"):
    if bool(angka) == True:
        print("Angka yang anda input adalah : " + str(angka))
    else:
        print(angka)
    
fungsi1(7)

# Contoh 2
def fungsi2(angka1,angka2 = 0):
    if bool(angka1 & angka2) == True:
        hasil = print(f"Hasil tmabah dari {angka1} + {angka2} adalah {angka1 + angka2}")
        return hasil
    else:
        print(f"Tidak ada angka dari {angka1} dan {angka2}")
        
fungsi2(15)
fungsi2(5,3)

# Contoh 3
def fungsi3(satu = 0, dua = 0):
    hasil = satu + dua
    return hasil

x = fungsi3(satu = 10)
print(x)
print(fungsi3(4, dua = 5))

# Contoh 4
def fungsi4(angka1 = 5, angka2 = 4, angka3 = 4, angka4 = 7):
    hasil = angka1 * angka2 * angka3 * angka4
    return hasil

print(fungsi4(7,angka3 = 8))
print(fungsi4(8,4,angka3 = 4))
print(fungsi4(angka3 = 8))
print(fungsi4())
