# BELAJAR OPERASI MANIPULASI STRING

## Menggunakan method untuk case
normal = "Kamu itu cakep"
upper = normal.upper()
print("Normal : " + normal)
print("Upper : " + upper)

normal = "KerEN AbisSssss"
lower = normal.lower()
print("Normal : " + normal)
print("Lower : " + lower)

## Menggunakan isX di method

# is cek semua Lower or upper case
nama = "SURUDIN MARSUDIN"
Upp = nama.isupper()
print(nama + " " + str(Upp))

nama = "Surudin marsudin"
Upp = nama.isupper()
print(nama + " " + str(Upp))

nama = "surudin marsudin"
low = nama.islower()
print(nama + " " + str(low))

nama = "Surudin marsudin"
low = nama.islower()
print(nama + " " + str(low))

# isalpha --> Untuk mengecek semua huruf 
nang = "Ini hanya huruf tapi ada spasi" # ada spasi
huru = nang.isalpha()
print(nang + " " + str(huru))

nang = "TanpaSpasi"
huru = nang.isalpha()
print(nang + " " + str(huru))

# isalnum --> untuk mengecek angka dan huruf
nang = "Ini hanya huruf tapi ada spasi2" # ada spasi
huru = nang.isalnum() 
print(nang + " " + str(huru))

nang = "TanpaSpasi2"
huru = nang.isalnum()
print(nang + " " + str(huru))

# isdecimal --> untuk mengecek semua angak
nang = "424 24" # ada spasi
huru = nang.isdecimal()
print(nang + " " + str(huru))

nang = "72648"
huru = nang.isdecimal()
print(nang + " " + str(huru))

# isspace --> untuk mengecek spasi, tab, \n, dll

nang = "kamu    kami" # hanya cek spasi, tab, \n, dll
huru = nang.isspace()
print(nang + " " + str(huru))

nang = "    \n"
huru = nang.isspace()
print(nang + " " + str(huru))

# istitle --> untuk mengecek semua di awali huruf besar

nang = "Siapa Pendekar Kuda Putih" 
huru = nang.istitle()
print(nang + " " + str(huru))

nang = "Keras D'dek" # ' di anggap sebagai awalan
huru = nang.istitle()
print(nang + " " + str(huru))

## Menggunkan startswith and endswith
start = "Kamu Surudin".startswith("Kamu")
print("Start adalah " + str(start))

end = "Kamu Surudin".endswith("Surudin")
print("End adalah " + str(end))

## Menggunkan join and split di string
judul = ["Pendekar","Singa","Loncat"]
join = " ".join(judul)
print("Normal " + str(judul) + " " + str(type(judul)))
print("Joinan " + join)

judul = ["Pendekar","Singa","Loncat"]
join = "-".join(judul)
print("Normal " + str(judul) + " " + str(type(judul)))
print("Joinan " + join)

judul = "pendekar-Singa-Loncat"
pisah = judul.split("-")
print("Normal " + judul)
print("Pisah pake split " + str(join) + " " + str(type(judul)))

## Menggunkan ljust, rjust and center
leftjust = "kiri".ljust(10)
print("'" + leftjust + "'")

leftjust = "KIRI".ljust(10,"=")
print("'" + leftjust + "'")

rightjust = "kanan".rjust(10)
print("'" + rightjust + "'")

rightjust = "KANAN".rjust(10,"=")
print("'" + rightjust + "'")

center = "center".center(10)
print("'" + center + "'")

center = "CENTER".center(10,"=")
print("'" + center + "'")

# strip menghapus dari alokasi karakter
stripl = leftjust.strip("=")
print("'" + stripl + "'")

stripr = rightjust.strip("=")
print("'" + stripr + "'")

stripc = center.strip("=")
print("'" + stripc + "'")
