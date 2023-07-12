# BELAJAR READ EXTERNAL FILE - OPEN AND WITH

file = open("text.txt",mode="r") # mode r(read) = Membaca, w(membaca) = menulis

print("="*3," Tutorial Membaca File ",3*"=")
# print(file.read()) Pakai Read untuk mencetak semua file

print(f"File ini apakah Bisa di Baca : {file.readable()}") 
print(f"File ini apakah Bisa di Baca : {file.writable()}") 

# print(file.readline()) # Mencetak satu baris
# # print(file.readline()) # Mencetak satu baris

# print(file.readlines()) # Untuk Cetak Semua Baris
# print(file.readlines(),end="") # pakai end untuk mengubah akhir string

print(file.readline(), end="") # pakai end untuk mengubah akhir string
print(file.readline(), end="") # pakai end untuk mengubah akhir string

print(f"Apakah file ini sudah diclose : {file.closed}")
file.close() # Setalah buka file jangan lupa untuk di close / tutup
print(f"Apakah file ini sudah diclose : {file.closed}")


# Menggunkan with untuk open file nya

print('\n',"="*3," Tutorial Membaca File Dengan With ",3*"=")

with open("text.txt",mode="r") as file2:
    # print(file.read()) 
    fileLine = file2.readline() # Jika pakai ini  yang terprint ke 2 sama dengan yang ke 1
    print(fileLine,end="") # 1
    print(fileLine,end="") # 2
    # print(file.readline()) # Berbeda dengan ini

    print(file2.read())
    print(f"Apakah file ini sudah diclose : {file2.closed}")

# Tinggal keluar dari with untuk close
print(f"Apakah file ini sudah diclose : {file2.closed}")

