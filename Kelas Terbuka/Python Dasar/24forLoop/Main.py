# LATIHAN FOOR LOP

# Pakai list
angka = [1,2,3,4,5,6,7]

print("PROGRAM MULAI".center(20,"="))
for i in angka:
    print(f"Angka sekarang adalah -> {i}")
print("PROGRAM SELESAI".center(20,"=") + "\n")

# Pakai range
print("PROGRAM MULAI".center(20,"="))
for i in range(4,15,2):
    print(f"Angka sekarang adalah -> {i}")
print("PROGRAM SELESAI".center(20,"=") + "\n")

# Pakai list
nama_c = "Ini karakter char"
print("PROGRAM MULAI".center(20,"="))

for i in nama_c:
    print(i)
print("PROGRAM SELESAI".center(20,"=") + "\n")

# Latihan
angka = [1,2,3,4,5,6,7,8,9,10]
kt = "*"
angka2 = range(2,10,2)

for i in angka:
    print(kt)
    kt += "*"
print("PROGRAM SELESAI".center(20,"=") + "\n")

for i in angka2:
    print(kt)
    kt += "*"
print("PROGRAM SELESAI".center(20,"=") + "\n")
