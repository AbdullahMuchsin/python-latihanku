## APLIKASI MENGHITUNG LUAS DAN KELILING SEGITIGA
import os
import math

def header():
    print(f"{'-'*40:^40}")
    print(f'{"PERHITUNGAN SEGITIGA":^40}')
    print(f'{"KELILING DAN LUAS":^40}')
    print(f"{'-'*40:^40}")

def luas_segitiga(alas,tinggi):
    luasSegitiga = (1/2) * alas * tinggi
    return luasSegitiga

def keliling_segitiga(sisi_a,sisi_b,sisi_c):
    return sisi_a + sisi_b + sisi_c

def tampilan(nama,nilai):
    print(f"Hasil Perhitungan {nama} adalah : {math.floor(nilai)}\n")

def select():
    print("""\n    1. Menghitung Luas Segitiga
    2. Menghitung Keliling Segitiga
    """)
    memilih = int(input("Masukan Nomor sesuai yang anda ingin kan : "))

    if memilih == 1:
        dataTinggi = int(input("Masukan tinggi segitiga : "))
        dataAlas = int(input("Masukan alas segitiga   : "))
    elif memilih == 2:
        sisi_a = int(input("Masukan sisi a segitiga : "))
        sisi_b = int(input("Masukan sisi b segitiga : "))
        sisi_c = int(input("Masukan sisi c segitiga : "))

    if memilih == 1:
        tampilan("luas", luas_segitiga(dataAlas,dataTinggi))
    elif memilih == 2:
        tampilan("keliling", keliling_segitiga(sisi_a, sisi_b, sisi_c))
    else:
        print("Nomor yang anda masukan tidak error!!!")

while True:
    os.system("cls")
    header()
    select()

    isOption = input("Apakah anda ingin keluar dari program (y/n) ?")
    if isOption == "y":
        break

print("\n","PROGRAM SELESAI".center(40,"="))