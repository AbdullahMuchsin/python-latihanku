from . import Operasi

def delete_console():
    read_console()
    while (True):
        no_buku = int(input("Masukan Nomor Buku : "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            
            data_break = data_buku.split(",")
            presskey = data_break[0]
            date_time = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            print("Ini adalah data yang akan di dalete")
            print(f"1. Judul \t:{judul:.40}")
            print(f"2. Penulis \t:{penulis:.40}")
            print(f"3. Tahun \t:{tahun:4}")

            isDone = input("Apakah anda yakin (y/n) : ")
            if isDone == "Y" or isDone == "y":
                Operasi.delete(no_buku)
                break
        else:
            print("Nomor yang anda masukan tidak valid !!!")
    print("Data berhasil dihapus !!!")

def update_console():
    read_console()
    while (True):
        no_buku = int(input("Masukan Nomor Buku : "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("Nomor yang anda masukan tidak valid !!!")
    
    data_break = data_buku.split(",")
    presskey = data_break[0]
    date_time = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while (True):
        print("Silahkan pilih data yang ingin anda ubah")
        print(f"1. Judul \t:{judul:.40}")
        print(f"2. Penulis \t:{penulis:.40}")
        print(f"3. Tahun \t:{tahun:4}")

        user_option = input("pilih data [1,2,3] : ")
        print("\n" + "="*100)
        match user_option:
            case "1" : judul = input("Judul \t:")
            case "2" : penulis = input("Penulis \t:")
            case "3" :
                while (True):
                    try:
                        tahun = int(input("Masukan Tahun Buku : "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun Harus angka, Masukan Tahun Lagi (yyyy)")
                    except:
                        print("Tahun Harus angka, Masukan Tahun Lagi (yyyy)")
            case _: print("Index yang anda masukan tidak cocok !!!")
        
        print(f"1. Judul \t:{judul:.40}")
        print(f"2. Penulis \t:{penulis:.40}")
        print(f"3. Tahun \t:{tahun:4}")

        Operasi.update(no_buku, presskey, date_time, penulis, judul, tahun)

        isDone = input("Apakah data sudah sesuai (y/n) : ")
        if isDone == "Y" or isDone == "y":
            break

def create_console():
    print("\n" + "="*100)
    penulis = input("Masukan Nama Penulis : ")
    judul = input("Masukan judul buku  : ")
    while (True):
        try:
            tahun = int(input("Masukan Tahun Buku : "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun Harus angka, Masukan Tahun Lagi (yyyy)")
        except:
            print("Tahun Harus angka, Masukan Tahun Lagi (yyyy)")
    
    Operasi.create(penulis, judul, tahun)
    print("\nBerikut adalah data baru anda : ")
    read_console()

def read_console():
    data_file = Operasi.read()

    index = "No"
    penulis = "Penulis"
    judul = "Judul"
    tahun = "Tahun"

    # Header
    print("\n" + "="*100)
    print(f"{index:^5} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)

    # Data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        
        presskey = data_break[0]
        date_time = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]

        print(f"{index + 1:^5} | {judul:.40} | {penulis:.40} | {tahun:5}",end="")

    # Flooter
    print("="*100 + "\n")

