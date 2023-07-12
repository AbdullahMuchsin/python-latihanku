## BELAJAR GLOBAL DAN LOCAL SCOPE

ANGKA = 18

# Akses variabel global dalam fungsi
def f_angka():
    print(f"Ini adalah isi dari variabel ANGKA :  {ANGKA}")

f_angka()

# Akses variabel global dalam for/loop
for i in range(5):
    print(f"Index ke-> {i} : {ANGKA}")

# Akses variabel global dalam if
if True:
    print(f"Ini adalah isi dari variabel ANGKA :  {ANGKA}")

## Variabel local scope

def variabel_local():
    angka = 18 # Ini variabel local scope berada dalam def/method
    return angka

variabel_local()
# print(angka) Tidak bisa dijalankan

# # Contoh penggunaan 1 variabel:
def variabel1():
    print(f"Ini adalah value dari variabel angka1 : {angka1}")

angka1 = 18 # Jika ini dibawah pemanggil fungsi maka error dan sebaliknya
variabel1() # Ini pemanggil fungsi

# Contoh 2 Merubah Variabel global

'''Jika seperti ini tidak bisa'''
NILAI = 15

def f_local(hasil):
    NILAI = hasil
    return NILAI

print(f"Tidak bisa {NILAI}")
f_local(6)
print(NILAI)
print(f_local(3))

'''Di dalam fungsi kasih code global variabel apa yang ingin dipilih'''
NILAI = 15
NAMA = "Marsudin"
def f_local(hasil, nama = "Noun"):
    global NILAI,NAMA
    NILAI = hasil
    NAMA = nama
    return NILAI,NAMA

print(f"Bisa {NILAI}")
print(f"Bisa {NAMA}")
f_local(6,"Surudin")
print(NILAI)
print(NAMA)
print(f_local(3))

# Variable global tidak bisa diganti hanya di dalam def(fungsi) di if dan loop bisa tetep diganti
HASIL = 0

for i in range(0,10):
    HASIL += i
    ANGKA_DALAM = 0

print("INI FOR")
print(HASIL)
print(ANGKA_DALAM)

if True:
    HASIL = 27
    ANGKA_DALAM =77

print("INI IF")
print(HASIL)
print(ANGKA_DALAM)

## TETAP BISA TERGANTI MESKI VARIABLE DIDALAM FOR ATAU IF BERBEDA DENGAN DEF(FUNGSI)