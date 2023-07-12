import datetime as dt
import os
import string
import random

## LATIHAN DICTIONARY

siswa_tamplate = {
    'nama' : 'nama',
    'nim' : 'nim',
    'lahir' : dt.datetime(1111,1,11),
    'kota' : 'kota',
    'kelas' : 'kelas'
}

newsiswa = {}

while True:
    os.system("cls")
    siswa = dict.fromkeys(siswa_tamplate.keys())

    print("-"*20)
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'SISWA BARU':^20}")
    print("-"*20)

    siswa['nama'] = input("Nama Siswa               : ")
    siswa['nim'] = input("NIM Siswa                : ")
    TAHUN_LAHIR = int(input("Tahun Lahir Anda(YYYY)   : "))
    BULAN_LAHIR = int(input("Bulan Lahir Anda(1-12)   : "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir Anda(1-31) : "))
    siswa['lahir'] = dt.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    siswa['kota'] = input("Kota Anda                : ")
    siswa['kelas'] = input("Kelas Anda               : ")

    KEY = ''.join((random.choice(string.ascii_uppercase)) for i in range(6))
    newsiswa.update({KEY:siswa})

    print(f"\n{'KEY':<6} {'NAMA':^17} {'NIM':^11} {'LAHIR':9} {'KOTA':^10} {'KELAS':^6}")

    for siswa in newsiswa.keys():
        KEY1 = siswa

        NAMA = newsiswa[KEY1]['nama']
        NIM = newsiswa[KEY1]['nim']
        LAHIR = newsiswa[KEY1]['lahir'].strftime("%x")
        KOTA = newsiswa[KEY1]['kota'].upper()
        KELAS = newsiswa[KEY1]['kelas']

        print(f"{KEY1:<6} {NAMA:^17} {NIM:^11} {LAHIR:^9} {KOTA:^9} {KELAS:^6}\n")
        

    xon = input("Apa anda ingin isi data lagi (y/n) ? ")
    
    if xon == "n":
        break
print("PROGRAM SELESAI".center(20,"="))



    




