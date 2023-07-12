# BELAHAR EXCEPTION
# Mengatasi runtime error yaitu error saat ditengah jalan(run)


# angka = int(input("Masukan angka tambah : "))

# hasil = 12/angka # contoh jika di bagi 0 atau dimaukan string akan error
# print(f"hasil nya adalah : {hasil}")

# Pakai try,Except : Example 1

while(True): 
    try: # Jika hasil tidak error maka try dijalankan
        angka = int(input("Masukan angka tambah : "))
        try:
            hasil = 10/angka
            break
        except:
            print("Angka Tidak Bolah 0")
    except:
        print("Hanya Masukan angka saja")

print(f"Hasil nya adalah {hasil}")

# Pakai try,Except Exception : Example 2

while(True): 
    try: # Jika hasil tidak error maka try dijalankan
        angka = int(input("Masukan angka tambah : ")) # ini yang erro jika dimasukan string
        try:
            hasil = 10/angka # ini yang erro jika dimasukan angka 0
            break
        except ZeroDivisionError as error_messegs: # Masukan nama error lebih bagus jika tau
            print(error_messegs)
    except Exception as error_messegs: # Pakai Exception aja gapapa
        print(error_messegs)

print(f"Hasil nya adalah {hasil}")

while (True):
    try:
        with open("text.txt",mode="r") as file:
            print(f"isi file text.txt adalah : \n{file.read()}")
        break
    except:
        print("file text.txt tdiak ditemukan, Membuat file baru!!!")
        with open("text.txt",mode="w",encoding="utf-8") as file:
            file.write("File baru")
        break

print("akhir program text.txt")

