# FIBBONACCI

batas = int(input("Masukan batas baris : "))
angka1, angka2 = 0,1
for i in range(batas):

    print(angka1, end=" ")

    gabungan = angka1 + angka2
    angka1 = angka2
    angka2 = gabungan
