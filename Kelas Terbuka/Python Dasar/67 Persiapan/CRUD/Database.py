from . import Operasi
TAMPLATE = {
    "presskey" : "XXXXXX",
    "date_time" : "yyyy-dd-mm",
    "penulis" : 200*" ",
    "judul" : 200*" ",
    "tahun" : "yyyy"
}

DB_NAME = "data.txt"

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("Database ada")
    except:
            print("Database tidak ditemukan, akan membuat database baru !!!")
            Operasi.create_first_data()
