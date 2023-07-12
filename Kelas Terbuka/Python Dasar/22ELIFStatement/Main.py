# LATIHAN OPERASI ELIF = ELSE IF STATEMENT

print("Daftar data".upper())
us = input("Masukkan username baru anda : ")
npas = input("Masukkan sandi baru anda    : ")
ks = input("Konfirmasi".upper() + " sandi baru anda  : ")

if npas == ks :
    print("\nisi data diri anda: ".upper())
    nama = input("Masukan nama anda : ")
    umur = int(input("Masukan umur anda : "))
    user = us
    sandi = npas
elif npas != ks :
    print("\nSandi yang anda masukan salah")
else:
    print("\nData yang anda masukan error")

print("\nSilahkan masukan username dan passwor dibawah untuk cek data anda: ")

kuser = input("Masukan username anda  : ")
kpas = input("Masukan sandi anda     : ")


if (kpas == ks) & (kuser == us):
    print("\ndata anda".upper())
    print(f"Nama anda adalah     : {nama}")
    print(f"Umur anda adalah     : {umur} Tahun")
    print(f"Username anda adalah : {us}")
    print(f"Sandi anda adalah    : {npas}")
elif (kpas != ks) | (kuser != us) :
    print("\nSandi yang anda masukan salah")
else:
    print("Data yang anda masukan error")
print("\nProgram telah selesai".upper())

