## LATIHAN KOMPARASI DAN LOGIKA

## Daerah penyelesaian

# +++++++++++0-----------5+++++++++++ (Menyambung)
print("+++++++++++0-----------5+++++++++++ (Menyambung)")
data = float(input("Masukan angka kurang dari 0 atau lebih dari 5 : "))

# ++++++++++++0---------
isKurangDari = data < 0
print(data,'<',0,'=',isKurangDari)

# --------5++++++++++++++
isLebihDari = data > 5
print(data,'>',5,'=',isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("Data yang anda masukan bernilai :",isCorrect)

# ---------0++++++++++++5---------- (Mengiris)
print("# ---------0++++++++++++5---------- (Mengiris)")
data = float(input("Masukan angka kurang dari 0 dan lebih dari 5 : "))

# ------------0+++++++
isKurangDari = data > 0
print(data,'>',0,'=',isKurangDari)

# +++++++5------------
isLebihDari = data < 5
print(data,'<',5,'=',isLebihDari)

isCorrect = isKurangDari and isLebihDari
print("Data yang anda masukan bernilai :",isCorrect)

## PR MEMBUAT DAERAH PENYELESAIN

# ----0++++5----10++++15----
print("----0++++5----10++++15----(Campuran)")
data2 = float(input("Masukan angka lebih dari 0 dan kurang dari 5 atau lebih dari 10 dan kurang dari 15 : "))

isLebihKurang1 = data2 < 5
isKurangLebih1 = data2 > 0
isCek1 = isLebihKurang1 and isKurangLebih1

isLebihKurang2 = data2 < 15
isKurangLebih2 = data2 > 10
isCek2 = isLebihKurang2 and isKurangLebih2

isCorrect1 = isCek1 or isCek2
print("Data yang anda masukan bernilai :",isCorrect1)

# ++++0----5++++10----15++++
print("++++0----5++++10----15++++(Campuran)")
data2 = float(input("Masukan angka kurang dari 0 atau lebih dari 5 dan kurang dari 10 atau lebih dari 15 : "))

isLebihKurang1 = data2 > 5
isKurangLebih1 = data2 < 0
isCek1 = isLebihKurang1 or isKurangLebih1

isLebihKurang2 = data2 > 15
isKurangLebih2 = data2 < 10
isCek2 = isLebihKurang2 or isKurangLebih2

isCorrect1 = isCek1 and isCek2
print("Data yang anda masukan bernilai :",isCorrect1)