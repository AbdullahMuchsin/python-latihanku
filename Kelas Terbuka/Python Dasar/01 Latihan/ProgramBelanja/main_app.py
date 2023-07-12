''' Membuat Program Belanja '''

""" 
    Struktur Belanja:
   1. daftar barang
   2. isi barang
   3. menghapus barang
   4. membeli barang
"""
import datetime as dt
import os, string, random

tample_isi_barang = {
    "nama" : "nama",
    "tanggal" : dt.datetime(1111,1,11),
    "harga" : 0
}

isi_barang = {}

def isi_b():
    os.system("cls")
    isiBarang = dict.fromkeys(tample_isi_barang.keys())

    isiBarang["nama"] = input("Silahkan Masukan Nama Barang : ")
    TANGGAL_BARANG = int(input("Masukan Tanggal Kadaluarsa Barang : "))
    BULAN_BARANG = int(input("Masukan Bulan Kadaluarsa Barang : "))
    TAHUN_BARANG = int(input("Masukan Tahun Kadaluarsa Barang : "))
    isiBarang["tanggal"] = dt.datetime(TANGGAL_BARANG,BULAN_BARANG,TAHUN_BARANG)
    isiBarang["harga"] = int(input("Silahkan Masukan Harga Barang : "))

    KEY = ''.join((random.choice(string.ascii_uppercase)) for i in range(4))
    
    isi_barang.update({KEY : isiBarang})

    return isi_barang

def menghapus_i(input_h):
    del isi_barang[input_h]
    return isi_barang

def display():
    print(f"{'KEY':^6}. | {'NAMA':^15}\t\t | {'HARGA':^10}\t | {'TANGGAL KADALUARSA':^20}")
    
    for kode in isi_barang.keys():
        KEY = kode

        NAMA = isi_barang["nama"]
        TANGGAL = isi_barang["tanggal"]
        HARGA = ["harga"]

    print(f"{KEY:^6}. | {NAMA:^15}\t\t | {HARGA:^10} | {TANGGAL:^20}")


while True:
    os.system("cls")
    print("-"*20)
    print("PROGRAM BELANJA".center(20))
    print("-"*20)

    print("""
    1. Melihat Daftar Barang
    2. Menambahkan Isi Barang
    3. Menghapus Isi Barang
    4. Membeli Barang
    """) 
    isSelect = int(input("Silahkan masukan nomor untuk memilih : "))

    if isSelect == 1:
        if isi_barang :
            print("Belum ada barang T_T")
        elif isi_barang != :
            display()