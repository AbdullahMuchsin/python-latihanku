from . import View

TAMPLATE = {
    "kunci" : " "*6,
    "nama" : " "*25,
    "waktu" : 1111,
    "penulis" : " "*25,
    "tahun" : 1111
}

DB_NAMA  = "data.txt"

def cek():
    try:
        with open(DB_NAMA,mode = "r") as file:
            print("Database Ada")
    except:
        View.viewbaru()