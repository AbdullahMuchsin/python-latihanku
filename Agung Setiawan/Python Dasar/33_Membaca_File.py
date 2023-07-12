try:
    file = open("Database/data.txt", mode="r")
except FileNotFoundError:
    print("File tidak ditemukan")

print(file.read()) # Membaca keseluruhan
print("===============================")
file.close()

try:
    file = open("Database/data.txt", mode="r")
except FileNotFoundError:
    print("File tidak ditemukan")
print(file.readline()) # Membaca satu baris di akhiri dengan enter
print(file.readline()) # Membaca satu baris di akhiri dengan enter
print(file.readline()) # Membaca satu baris di akhiri dengan enter
print("===============================")
file.close()

try:
    file = open("Database/data.txt", mode="r")
except FileNotFoundError:
    print("File tidak ditemukan")

array = file.readlines() # Memjadikan list dengan satu baris sama dengan satu item
print("===============================")

print(array[2])
print("===============================")
file.close()

try:
    file = open("Database/data.txt", mode="r")
except FileNotFoundError:
    print("File tidak ditemukan")
index = 1
for i in array:
    print(f"{index}. {i}")
    index += 1
print("===============================")
