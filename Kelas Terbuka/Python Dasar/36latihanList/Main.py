import os
## LATIHAN KE LIMA LIST
# Membuat daftar buku

list_buku = []

while True:
    os.system("cls")
    print("\n","APLIKASI DAFTAR BUKU".center(35,"="),"\n")
    print("""    1. Menambahkan daftar buku
    2. Menampilkan daftar buku
    3. Mengecek daftar buku
    4. Menghapus daftar buku
    5. Menutup Program
    """)
    inp = int(input("Masukan angka sesuai yang anda inginkan : "))

    if inp == 1:
        jd1 = input("Masukan judul buku     : ")
        nm1 = input("Masukan pengarang buku : ")

        bkn = [jd1,nm1]
        list_buku.append(bkn)
        x = input("Apakah mau keluar? (y/n)")
        if x == "y":
            break
    elif inp == 2:
        print("No.\t| Judul \t| Nama")
        for index,data in enumerate(list_buku):
            print(f"{index + 1}.\t| {data[0]}\t| {data[1]}")

        x = input("Apakah mau keluar? (y/n)")
        if x == "y":
            break
    elif inp == 3:
        cek1 = input("Masukan judul buku : ")
        cek2 = input("Masukan pengarang buku : ")

        if [cek1,cek2] in list_buku:
            incek = list_buku.index([cek1,cek2])
            print(f"Buku berada pada Nomor : {incek + 1}")
            print(f"No.\t| Judul\t| Nama")
            for index, data in enumerate(list_buku):
                print(f"{index + 1}.\t| {data[0]}\t| {data[1]}")
        else:
            print("Maaf buku yang anda cari tidak ada!!!")
            
        x = input("Apakah mau keluar? (y/n)")
        if x == "y":
            break
    elif inp == 4:
        inx = int(input("Silahkan masukan indext daftar buku yang ingin dihapus : "))
        pl = len(list_buku)
        if inx > (pl-1): 
            print("Daftar list yang anda masukan tidak ada")
        else:
            list_buku.remove(list_buku[inx])
        x = input("Apakah mau keluar? (y/n)")
        if x == "y":
            break
    elif inp == 5:
        break
    else:
        print("Angka yang anda masukan tidak ada, coba ulangi lagi!!!")
print("PROGRAM BERAKHIR".center(35,"="))