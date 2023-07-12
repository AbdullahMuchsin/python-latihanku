## BELAJAR LAMBDA FUNGSI

def pangkat(nilai,n):
    return nilai**n
HASIL = pangkat(2,4)
print(HASIL)

# Menggunakan lambda
pangkat2 = lambda x:x**2
print(f"Hasil dari pangkat 2 tersebut adalah : {pangkat2(2)}")

pangkat = lambda x,y: x**y
print(f"Hasil dari pangakt n adalah : {pangkat(2,4)}")

# Sort pada list
data_list = ["Surudin", "Marsudin", "Udin"]
data_list.sort()
print(f"Data sort list biasa : {data_list}")

data_list.sort(key=len)
print(f"Data sort list biasa dengan len : {data_list}")

def sort_list(data):
    return len(data)

data_list.sort(key = sort_list)
print(f"Data sort list biasa dengan len fungsi: {data_list}")

# Dengan sort lambda
data_list.sort(key = lambda nama:len(nama)) # sama saja
print(f"Data sort list biasa dengan len lambda: {data_list}")

data_list.sort(key = lambda nama:len(nama)) # Dengan ini
print(f"Data sort list biasa dengan len lambda: {data_list}")

# Fillter
angka_list = [1,3,52,5,62,62,1,3,2,52,1,3,34]

def filter_kurang(angka):
    return angka < 20

OUTPUT = list(filter(filter_kurang,angka_list))
print(f"Hasil filter tersebut adalah : {OUTPUT}")

OUTPUT = list(filter(lambda nilai:nilai > 30, angka_list))
print(f"Hasil filter tersebut adalah : {OUTPUT}")

# Hasil genap
OUTPUT = list(filter(lambda nilai:(nilai%2 == 0), angka_list))
print(f"Hasil genap filter tersebut adalah : {OUTPUT}")

# Hasil ganjil
OUTPUT = list(filter(lambda nilai:(nilai%2 != 0), angka_list))
print(f"Hasil ganjil filter tersebut adalah : {OUTPUT}")

# Keliptan 4
OUTPUT = list(filter(lambda nilai:(nilai%4 == 0), angka_list))
print(f"Hasil kelipatan 4 filter tersebut adalah : {OUTPUT}")

# Anonymous function
# Currying -> Haskell Curry

# def biasa
def f_fungsi(n,x):
    return n**x

OUT = f_fungsi(2,5)
print(f"Hasil dari Fungsi f_function adalah : {OUT}")

# def dengan function
def f_function(n):
    return lambda x : x**n

NILAI = f_function(2) # Input untuk def(f_function) nya
print(f"Hasil dari Fungsi f_function adalah : {NILAI(3)}") # Yang ini input untuk lambda

NILAI = f_function(5) # Input untuk def(f_function) nya
print(f"Hasil dari Fungsi f_function adalah : {NILAI(3)}") # Yang ini input untuk lambda
