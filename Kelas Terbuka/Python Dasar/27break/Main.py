# LATIHAN MENGGUNKAN CODE BREAK

# Contoh satu (1)
nama = ["Surudin", "Marsudin", "Budi", "Doni", "Danang", "Sari"]

print("PROGRAM MULAI".center(25,"="))
for na in nama:
    if na == "Budi":
        print("Kamu siapa ga kenal...")
        continue
    elif na == "Danang":
        print(f"Last Hai {na}")
        break
    print(f"Hai {na}")
print("PROGRAM BERAKHIR".center(25,"=") + "\n")

# Contoh dua (2)
print("PROGRAM MULAI".center(25,"="))
inp = int(input("Masukan batas angka looping : "))
st = 0
while True:
    st += 1
    if st == 10:
        print("Ini angka lewatin dulu ga si..")
        continue
    elif st == inp :
        print(f"Stop dulu ga sih sudah angka {st}")
        break
    print(f"Angka sekarang adalah : {st}")
print("PROGRAM BERAKHIR".center(25,"="))