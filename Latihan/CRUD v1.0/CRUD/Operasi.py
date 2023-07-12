from . import Util
from . import Database
import datetime
import os

def fileHapus(memilih):
    try:
        with open(Database.DB_NAMA, mode = "r") as file:
            jumblah = 0
            while True:
                data = file.readline()
                if len(data) == 0:
                    break
                elif jumblah == memilih:
                    pass
                else:
                    with open("data_copy.txt",mode="a",encoding="utf-8") as file_c:
                        file_c.write(data)
                jumblah += 1
    except:
        print("Database Erro")
    os.replace("data_copy.txt",Database.DB_NAMA)

def filePerbarui(nomor,kunci,nama,waktu,penulis,tahun):
    fileC = Database.TAMPLATE.copy()

    fileC["kunci"] = kunci
    fileC["nama"] = nama + (" "*(25 - len(nama)))
    fileC["waktu"] = waktu
    fileC["penulis"] = penulis + (" "*(25 - len(penulis)))
    fileC["tahun"] = tahun

    str_file = f"{fileC['kunci']}/{fileC['nama']}/{fileC['waktu']}/{fileC['penulis']}/{fileC['tahun']}" 
    panjang = len(str_file)
    try:
        with open(Database.DB_NAMA, mode = "r+", encoding = "utf-8") as file:
            file.seek(panjang * (nomor - 1))
            file.write(str_file)
    except:
        print("Database error")

def fileTambah(nama,penulis,tahun):
    fileC = Database.TAMPLATE.copy()

    fileC["kunci"] = Util.rand(6)
    fileC["nama"] = nama + (" "*(25 - len(nama)))
    fileC["waktu"] = datetime.datetime.today().strftime("%Y")
    fileC["penulis"] = penulis + (" "*(25 - len(penulis)))
    fileC["tahun"] = tahun

    str_file = f"{fileC['kunci']}/{fileC['nama']}/{fileC['waktu']}/{fileC['penulis']}/{fileC['tahun']}\n"

    try:
        with open(Database.DB_NAMA, mode = "a", encoding = "utf-8") as file:
            file.write(str_file)
    except:
        print("Database error")

def fileBaru(nama,penulis,tahun):
    fileC = Database.TAMPLATE.copy()

    fileC["kunci"] = Util.rand(6)
    fileC["nama"] = nama + (" "*(25 - len(nama)))
    fileC["waktu"] = datetime.datetime.today().strftime("%Y")
    fileC["penulis"] = penulis + (" "*(25 - len(penulis)))
    fileC["tahun"] = tahun

    str_file = f"{fileC['kunci']}/{fileC['nama']}/{fileC['waktu']}/{fileC['penulis']}/{fileC['tahun']}\n"

    try:
        with open(Database.DB_NAMA, mode = "w", encoding = "utf-8") as file:
            file.write(str_file)
    except:
        print("Database error")
    
def Memilih(**angka):
    try:
        with open(Database.DB_NAMA, mode = "r") as file:
            data = file.readlines()
            jumblah_data = len(data)
            if "pilih" in angka:
                nomor = (angka["pilih"] - 1)
                if nomor < 0 or nomor > jumblah_data:
                    return False
                else :
                    return data[nomor]
            else:
                return data
    except:
        print("Database error")
