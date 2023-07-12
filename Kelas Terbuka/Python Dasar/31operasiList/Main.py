## BELAJAR MENGGUNAKAN OPERASI LIST

dataAngka = [12,3,1,4,5,7,36,3,32,3,1]
dataString = ["Lemon", "Leci", "Pisang", "Mangga"]
print(f"Data angka : {dataAngka}")
print(f"Data angka : {dataString}")

# Menghitung list
print("\n1. Menghitung list dengan count")
jumblahData = len(dataAngka)
data1 = dataAngka.count(1)
data4 = dataAngka.count(4)
print(f"Jumblah data : {jumblahData}")
print(f"Jumblah ke-1 : {data1}")
print(f"Jumblah ke-4 : {data4}")

# Mencari index list
print("\n2. Mencari index list")
indexs1 = dataString.index("Pisang")
indexs2 = dataString.index("Lemon")
print(f"Index dari Pisang adalah : {indexs1}")
print(f"Index dari Lemon adalah : {indexs2}")

# Mengurutkan data list
print("\n3. Mengurutkan data list")
print(f"Data angka sebelum urut : \n {dataAngka}")
print(f"Data string sebelum urut : \n {dataString}")
angkas = dataAngka.sort()
strings = dataString.sort()
print(f"Data angka setelah urut : \n {dataAngka}")
print(f"Data string setelah urut : \n {dataString}")

# Membalikkan list dengan reverse
print("\n4. Membalikkan list dengan reverse")
print(f"Data angka sebelum dibalik : \n {dataAngka}")
print(f"Data string sebelum dibalik : \n {dataString}")
angkas = dataAngka.reverse()
strings = dataString.reverse()
print(f"Data angka setelah dibalik : \n {dataAngka}")
print(f"Data string setelah dibalik : \n {dataString}")
