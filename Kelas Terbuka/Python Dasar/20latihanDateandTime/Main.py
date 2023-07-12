# BELAJAR MEMBUAT DATE AND TIME
import datetime as dt

ln = "APLIKASI SEDERHANA CEK UMUR"
hn = ln.center(35,"=")
print(hn)

# 1. Step one
nu = "Silahkan isi data lahir anda di bawah ini\n".upper()
print(nu)

tanggal = input("Masukkan tanggal lahir anda\t: ")
bulan = input("Masukkan bulan lahir anda\t: ")
tahun = input("Masukkan tahun lahir anda\t: ")
st = int(tahun)
sb = int(bulan)
sl = int(tanggal)
tgl_l = dt.date(st,sb,sl)

# 2. Step two
td = dt.date.today()
wu = td - tgl_l
tgl_tahun   = (wu.days // 365)
tgl_bulan   = ((wu.days % 365) // 30 )
tgl_tanggal = ((wu.days % 365) % 30 )

# 3. Hasil or Print
print(f"\nTanggal lahir anda adalah   : {tgl_l}")
print(f"Hari lahir anda adalah hari : {tgl_l:%A}")
print(f"Umur anda sekarang adalah {tgl_tahun} Tahun - {tgl_bulan} Bulan - {tgl_tanggal} Hari\n")

# 4. Tambahan biar bagus
print("DATA ANDA".center(35,"="))
print(f"Tanggal sekarang adalah : {td}")
print(f"Hari sekarang adalah    : {td:%A}")
