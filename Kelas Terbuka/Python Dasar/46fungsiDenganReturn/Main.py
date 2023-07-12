import math
## BELAJAR FUNGSI DAN RETURN

'''
Template Funsi dan Return

def Fungsi(Input):
        Isi Fungsi
        return Output
'''

# Dengan Fungsi
def fungsi_x(variable_x):
    hasil_x = math.sqrt(variable_x) # math.sqrt() Berfungsi mengembalikan nilai kuadrat
    return hasil_x

x = fungsi_x(25)
print("Akar dari 25 adalah",x)

# Return langsung tanpa variable
def perkalian_pi(angka_x):
    hasil_x = angka_x * math.pi
    return hasil_x

print("Hasil dari nilai tersebut adalah :",perkalian_pi(2))

gabung = 15 + perkalian_pi(1)
print("Hasil nilai gabung tersebut adalah : " + str(gabung))

# Return langsung dan dua input
def modulus(nilai_k,nilai_m):
    return nilai_k % nilai_m

print("Hasil dari modulus tersebut adalah : " + str(modulus(10,3)))

# Return banyak
def artimatika(nilai_x,nilai_y):
    hasil_tambah = nilai_x + nilai_y
    hasil_kuranng = nilai_x - nilai_y
    hasil_kali = nilai_x * nilai_y
    hasil_pembagian = nilai_x / nilai_y

    return hasil_tambah, hasil_kuranng, hasil_kali, hasil_pembagian

x = artimatika(2,4) # Semua
a,b,c,d = artimatika(4,4) # Sendiri-Sendiri

print(f"Hasil semua adalah : {x}")
print(f"Hasil tambah adalah : {a}")
print(f"Hasil kurang adalah : {b}")
print(f"Hasil kali adalah : {c}")
print(f"Hasil pembagian adalah : {d}")




