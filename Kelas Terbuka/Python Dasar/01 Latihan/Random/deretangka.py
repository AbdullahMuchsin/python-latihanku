print("Angka ganjil")
batas = int(input("Masukan batas deret : "))

for i in range(batas):
    if (i%2):
        print(i,end=" ")

print("\nAngka genap")
batas = int(input("Masukan batas deret : "))

for i in range(batas):
    if (i%2) == 0:
        print(i,end=" ")

print("\nAngka ganjil")
batas = int(input("Masukan batas awal deret : "))
akhir = int(input("Masukan batas akhir deret : "))

for i in range(batas,akhir):
    if (i%2) != 0:
        print(i,end=" ")

print("\nAngka genap")
batas = int(input("Masukan batas awal deret : "))
akhir = int(input("Masukan batas akhir deret : "))

for i in range(batas,akhir):
    if (i%2) == 0:
        print(i,end=" ")