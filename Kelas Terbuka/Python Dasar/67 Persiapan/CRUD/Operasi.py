from . import Database
from . import Util
import time
import os

def delete(nomor_buku):
    try:
        with open(Database.DB_NAME,mode='r') as file:
            counter = 0
            while (True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == nomor_buku - 1:
                    pass
                else:
                    with open("data_temp.txt",mode='a', encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("Database Error !!!")

    os.replace("data_temp.txt",Database.DB_NAME)

def update(no_buku, presskey, date_time, penulis, judul, tahun):
    data = Database.TAMPLATE.copy()

    data["presskey"] = presskey
    data["date_time"] = date_time
    data["penulis"] = penulis + Database.TAMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TAMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    data_str = f'{data["presskey"]},{data["date_time"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    panjang_data =  len(data_str)

    try:
        with open(Database.DB_NAME,mode="r+",encoding="utf-8") as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("Aplikasi sedang error")

def create(penulis, judul, tahun):
    data = Database.TAMPLATE.copy()

    data["presskey"] = Util.random_string(6)
    data["date_time"] = time.strftime("%Y-%m-%d-%H-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TAMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TAMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    data_str = f'{data["presskey"]},{data["date_time"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME,mode="a",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Aplikasi sedang error")

def create_first_data():
    data = Database.TAMPLATE.copy()

    penulis = input("Masukan nama penulis : ")
    judul = input("Masukan judul buku : ")
    while (True):
        try:
            tahun = int(input("Masukan Tahun Buku : "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun Harus angka, Masukan Tahun Lagi (yyyy)")
        except:
            print("Tahun Harus angka, Masukan Tahun Lagi (yyyy)")

    data["presskey"] = Util.random_string(6)
    data["date_time"] = time.strftime("%Y-%m-%d-%H-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TAMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TAMPLATE["judul"][len(judul):]
    data["tahun"] = tahun


    data_str = f'{data["presskey"]},{data["date_time"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME,mode="w",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Aplikasi sedang error")

def read(**kwargs):
    try:
        with open(Database.DB_NAME,mode="r") as file:
            console = file.readlines()
            jumblah_buku = len(console)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumblah_buku:
                    return False
                else:
                    return console[index_buku]
            else:
                return console
    except:
        print("Mencari Database Error")
        return False