import string, datetime, os

def header(head : string) -> string:
    print("-"*20)
    print(head.center(20))
    print("-"*20)

def display(nama, umur, tanggal):
    os.system("cls")
    header("DATA ANDA")
    print(f"Nama  : {nama}")
    print(f"Umur  : {umur}")
    print(f"Lahir : {tanggal}")

''' Progam Utama '''

header("SELAMAT DATANG")

nama = input("Masukan Nama anda : ")
umur = int(input("Masukan Umur Anda : "))
TANGGAL = int(input("Masukan Tanggal Lahir Anda (1-31): " ))
BULAN = int(input("Masukan Bulan Lahir Anda (1-12) : "))
TAHUN = int(input("Masukan Tahun Lahir Anda (YYYY) : "))
tanggal_lahir = datetime.datetime(TAHUN,BULAN,TANGGAL).strftime("%x")

display(nama, umur, tanggal_lahir)





