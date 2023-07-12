## BELAJAR LOOPING LIST AND ENUMERATE

# Menggunakan for list
print("1. Menggunakan for list")
a = [1,4,3,7,9,10]
s = ["Jarjit","Surudin","Marsudin","Nopal"]

for angka in a:
    print(f"Angka : {angka}")

for string in s:
    print(f"string : {string}")

# Menggunkan for renge list
print("\n2. Menggunakan for range list")
a = [1,"Jarjit",2,"Surudin",5,"Marsudin",3,"Nopal"]

panjangl = len(a)
for angka in range(panjangl):
    print(f"data ke-{angka} : {a[angka]}")

# Menggunakan while list
print("\n3. Menggunakan while list")
a = [1,"Jarjit",2,"Surudin",5,"Mursid",3,"Nopal"]

panjangl = len(a)
angkaw = 0

while angkaw < panjangl:
    print(f"data ke-{angkaw} : {a[angkaw]}")
    angkaw += 1

# Menggunakan list comprehension
print("\n4. Menggunakan list comprehension")

a2 = [2,34,24,22,525,25,42]
a2.sort()
[print(f"angka : {i}") for i in a2]

# Menggunakan enumerate
print("\n5. Menggunakan enumerate")
a2 = [2,34,24,22,525,25,42]

for index,data in enumerate(a2):
    print(f"Index ke-{index}, Data ke-{data}")

# Menggunaka list comprehension variasi
print("\n6. Menggunakan list comprehension untuk variasi")

av = range(1,10,3)

[print(f"Angka ke pangkat ke-{i**2}") for i in av]