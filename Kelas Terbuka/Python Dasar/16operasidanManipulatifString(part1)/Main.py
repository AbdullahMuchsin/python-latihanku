## LATIHAN OPERASI DAN MANIPULASI STRING

# 1. Menggabungkan string
nama_awal = "Doni"
nama_tengah = "D"
nama_akhir = "Red"

nama_lengkap = nama_awal + " " + nama_tengah + "." + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string pakai len(lenght)
# # Pengurutan nomor dari angka 1 jika len(lenght)
panjang_nama = len(nama_lengkap)
print("Panjang nama",nama_lengkap,"adalah " + str(panjang_nama))

# 3. Mengecek karakter or kalimat di string

# in mengecek ada karakter or kalimat tesebut atau tidak
d = "d"
cek_1 = d in nama_lengkap
print("Karakter or Kalimat " + d + " di " + nama_lengkap + " adalah " + str(cek_1))

k = "k"
cek_1 = k in nama_lengkap
print("Karakter or Kalimat " + k + " di " + nama_lengkap + " adalah " + str(cek_1))

# not in mengecek tidak ada karakter or kalimat tesebut atau ada
doni = "Doni"
cek_1 = doni not in nama_lengkap
print("Karakter or Kalimat " + doni + " di " + nama_lengkap + " adalah " + str(cek_1))

doni = "doni"
cek_1 = doni not in nama_lengkap
print("Karakter or Kalimat " + doni + " di " + nama_lengkap + " adalah " + str(cek_1))

# 4. Mengecek nilai terbesar dan terkecil chr string
big_chr = max(nama_lengkap)
print("Karakter dari nama", nama_lengkap,"yang paling tinggi adalah",big_chr)

small_chr = min(nama_lengkap)
print("Karakter dari nama " + nama_lengkap + " yang paling rendah adalah " + small_chr)

# Melihat nilai karakter
cekK = ord(" ")
print("Nilai dari karakter ASCII CODE ' ' adalah",str(cekK))

ceko = ord("o")
print("Nilai dari karakter ASCII CODE ' ' adalah",str(ceko))

# Melihat karakter dari nilai
cekK = 42
print("Nilai 46 berupa karakter",chr(cekK))

ceko = 111
print("Nilai 111 berupa karakter",chr(ceko))

# Mengulang string
data = "hai"
print(10*data)
print(5*"hi")

# Indexing 
# Pengurutan nomor dari angka 0 jika indexing
print("Idex " + nama_lengkap + " dari ke-1 adalah " + nama_lengkap[0])
print("Idex " + nama_lengkap + " dari ke-2 adalah " + nama_lengkap[1])
print("Idex " + nama_lengkap + " dari ke-3 adalah " + nama_lengkap[2])
# Mengambil dari ex. 1-5 angka terakhir di tambah 1
print("Idex " + nama_lengkap + " dari ke-2: adalah " + nama_lengkap[1:4])
# Mengambil dari angka lompatan 2,4,6,8 akhiran di kasih tambah berapa lompatan
print("Idex " + nama_lengkap + " dari ke-0 adalah " + nama_lengkap[0:10:2])

# 5. Method pada string
judul = "Suara hati yang masih terpendam dalam lubuk hati ini"
banyak = judul.count("a")
print('Banyak karakter "a" di judul:' + judul +' Tersebut adalah ' + str(banyak))
