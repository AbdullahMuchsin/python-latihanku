from . import Operasi

TAMPLATE = {
    "presskey" : "XXXXXX",
    "date_time" : "yyyy-dd-mm",
    "nama" : 200*" ",
    "harga" : 200*" ",
    "tahun" : "yyyy"
}

DB_NAME = "data.txt"
def cekIn():
    try:
        with open(DB_NAME,mode='r') as file :
            print("Database Ditemukan")
    except:
        print("Database tidak ditemukan, membuat database Baru")
        Operasi.create_of_first()