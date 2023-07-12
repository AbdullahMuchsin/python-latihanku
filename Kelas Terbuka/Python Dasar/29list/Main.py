# LATIHAN LIST

print("1. Menggunakan list dengan Angka")
# 1. Menggunakan list dengan angka
angka = [1,5,4,5,1,7,8,9]
print(angka)

print("\n2. Menggunakan list dengan String")
# 2. Menggunakan list dengan string
kalimat = ["Surudi", "Marsudin", "Udin"]
print(kalimat)

print("\n3. Menggunakan list dengan Boolean")
# 3. Menggunakan list dengan boolean
trufal = [True, False, True, True]
print(trufal)

print("\n4. Menggunakan list dengan Campuran")
# 4. Menggunakan list dengan campuran
campuran = [1,"Surudin",2,"Marsudin",3,"Udin",True]
print(campuran)

print("\n5. Menggunakan list dengan Range")
# 5. Menggunkan list range
range_list = range(0,10,2)
print(range_list)
p_range_list = list(range_list)
print(p_range_list)

print("\n6. Menggunakan list dengan for untuk list")
# 6. Menggunakan list dengan for untuk list
list_for = [i*5 for i in range(0,10,2)]
print(list_for)

print("\n7. Menggunakan list dengan for untuk list and if ganjil")
# 7. Menggunakan list dengan for untuk list and if ganjil
list_for_it = [i*5 for i in range(0,10) if i%2 == True]
print(list_for_it)

print("\n8. Menggunakan list dengan for untuk list and if genap")
# 8. Menggunakan list dengan for untuk list and if genap
list_for_it = [i*5 for i in range(0,10) if i%2 != True]
print(list_for_it)

print("\n9. Menggunakan list dengan for untuk list and if")
# 9. Menggunakan list dengan for untuk list and if
list_for_c= [i*5 for i in range(0,10) if i == 5]
print(list_for_c)