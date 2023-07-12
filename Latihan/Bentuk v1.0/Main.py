try:
    row = int(input("Masukan panjang baris : "))
except:
    print("Angka tidak valid")
# kubus
print("Kubus")
for i in range(row):
    print("*"*row)

try:
    row = int(input("Masukan panjang baris : "))
except:
    print("Angka tidak valid")

# Segitiga Siku-Siku
print("Segitiga Siku-Siku")
for i in range(1,row + 1):
    print("*"*i)

try:
    row = int(input("Masukan panjang baris : "))
except:
    print("Angka tidak valid")

# Segitiga Siku-Siku Kebalik 1
print("Segitiga Siku-Siku Kebalik 1")
for i in range(row):
    print("*"*row)
    row -= 1

try:
    row = int(input("Masukan panjang baris : "))
except:
    print("Angka tidak valid")

# Segitiga Siku-Siku Kebalik 2
print("Segitiga Siku-Siku Kebalik 2")
for i in range(1,row + 1):
    print(" "*(row-i) + (i*"*"))

# Piramida
print("Piramida")
for i in range(1,row + 1):
    print(" "*(row-i) + (i*"*") + (i-1)*"*")

# Piramida Kebalik 
print("Piramida Kebalik")
kanan = row
for i in range(1,row + 1):
    print((i-1)*" " + (row-i)*"*" + (kanan)*"*")
    kanan -= 1
try:
    row = int(input("Masukan panjang baris : "))
except:
    print("Angka tidak valid")

# Wajik
print("Wajik")
for i in range(1,row + 1):
    print(" "*(row-i) + (i*"*") + (i-1)*"*")
kanan = row - 2
for i in range(1,row + 1):
    print((i)*" " + (row-i)*"*" + (kanan)*"*")
    kanan -= 1

# Jam
print("Jam")
kanan = row - 2
for i in range(1,row + 1):
    print((i)*" " + (row-i)*"*" + (kanan)*"*")
    kanan -= 1
for i in range(1,row):
    print(" "*(row-i) + (i*"*") + (i-1)*"*")

# Piramida angka
print("Piramida Angka")
for i in range(1,row + 1):
    print((row - i)*" ", end="")
    kanan = i
    kiri = 2
    for j in range(i):
        if i == 1:
            print(str(kanan),end="")
        else:
            print(str(kanan),end="")
        kanan -= 1
    for k in range(i-1):
        print(kiri,end="")
        kiri += 1
    print("")
