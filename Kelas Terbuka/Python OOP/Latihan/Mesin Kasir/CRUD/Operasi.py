from . import Database
from . import Randomkey
import time, os

def delete_item(index_input):
    try:
        with open(Database.DB_NAME,mode="r") as file:
            console = 0
            while True:
                datafile = file.readline()
                if len(datafile) == 0:
                    break
                elif console == index_input - 1:
                    pass
                else:
                    with open("Data_Copy.txt",mode="a",encoding="utf-8") as file_c:
                        file_c.write(datafile)
                console += 1
    except:
        print("Database Error")
    try:
        os.replace("Data_Copy.txt",Database.DB_NAME)
    except:
        print("Error Delete")
    
def update_item(no_buku,presskey,datetime,nama,harga,tahun):
    data = Database.TAMPLATE.copy()

    data["presskey"] = presskey
    data["date_time"] = datetime
    data["nama"] = nama + Database.TAMPLATE["nama"][len(nama):]
    data["harga"] = harga + Database.TAMPLATE["harga"][len(harga):]
    data["tahun"] = tahun 

    data_str = f'{data["presskey"]},{data["date_time"]},{data["nama"]},{data["harga"]},{data["tahun"]}\n'
    
    panjang_data = len(data)
    
    try:
        with open(Database.DB_NAME,mode="r+",encoding="utf-8") as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("Aplikasi sedang error")

def new_item(NAMA,HARGA,TAHUN):
    data = Database.TAMPLATE.copy()

    data["presskey"] = Randomkey.random_key(6)
    data["date_time"] = time.strftime("%Y-%m-%d-%H-%S%z",time.gmtime())
    data["nama"] = NAMA + Database.TAMPLATE["nama"][len(NAMA):]
    data["harga"] = HARGA + Database.TAMPLATE["harga"][len(HARGA):]
    data["tahun"] = TAHUN 

    data_str = f'{data["presskey"]},{data["date_time"]},{data["nama"]},{data["harga"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME,mode="a",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Aplikasi sedang error")
def create_of_first():
    data = Database.TAMPLATE.copy()

    NAMA = input("Masukan Nama Barang : ")
    while True:
        try:
            HARGA = str(int(input("Masukan Harga Barang : ")))
            break
        except:
            print("Masukan Angka")
    while True:
        try:
            TAHUN = int(input("Masukan Tahun Barang : "))
            if len(str(TAHUN)) == 4:
                break
            else:
                print("Tahun tidak boleh kurang dari 4 dan lebih dari 4")
        except:
            print("Masukan Angka")

    data["presskey"] = Randomkey.random_key(6)
    data["date_time"] = time.strftime("%Y-%m-%d-%H-%S%z",time.gmtime())
    data["nama"] = NAMA + Database.TAMPLATE["nama"][len(NAMA):]
    data["harga"] = HARGA + Database.TAMPLATE["harga"][len(HARGA):]
    data["tahun"] = TAHUN 

    data_str = f'{data["presskey"]},{data["date_time"]},{data["nama"]},{data["harga"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME,mode="w",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Aplikasi sedang error")
    
def read(**kwargs):
    try:
        file = open(Database.DB_NAME, mode="r")
        console = file.readlines()
        if "index" in kwargs:
            index_kwargs = kwargs["index"] - 1
            if index_kwargs < 0 or index_kwargs > len(console):
                return False
            else:
                return console[index_kwargs]
        return console
    except:
        print("Database error")
