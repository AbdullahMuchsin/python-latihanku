## BELAJAR CONTINUE AND PASS

# Pakai contiunue berfungsi meng cut dan melanjutkan eksekusi berikutnya
print(5*"=" + "MULAI PROGRAM" + 5*"=")
str = 0
while str < 5:
    str += 1
    if (str == 2) | (str == 4):
        print("Ini genap jadi genap lewatin dulu ga sii! ")
        continue
    print(f"Angka sekarang adalah : {str}")
print(5*"=" + "AKHIR PROGRAM" + 5*"=" + "\n")

# pass tidak adan dieksekusi
print(5*"=" + "MULAI PROGRAM" + 5*"=")
str = 0
while str < 5:
    str += 1
    if (str == 2) | (str == 4):
        print("Ini genap jadi genap lewatin dulu ga sii! ")
        pass
    print(f"Angka sekarang adalah : {str}")
print(5*"=" + "AKHIR PROGRAM" + 5*"=")
