## BELAJAR STRING
data = "Ini adalah string"
print(data, type(data))

# 1. Membuat string dengan quote
'''
    1. Menggunakan single quote '...'
    2. Menggunakan double quote "..."
'''

data1 = 'Ini menggunkan single quote'
print(data1)
data2 = "Ini menggunakan double quote"
print(data2)

# Bisa di gabungkan 
print('"Hai, kamu sedang apa?"')
print("Hai juga saya sedang ma'kan")

# Menggunakan \ di String

# Menambahkan ' pakai \' agar tidak error
print('Doni sedang ma\'kan')

# Menambahkan tab pakai \t
print("si A\tB sedang jauhan")
print("si A\t\t\tB sedang lebih jauhan")

# Menambahkan \ pakai \\ agar tidak error
print("C:budi\\new line")

# Menambahkan backspase pakai \b
print("Ini deketan \bdengan ini")

# Menambahkan enter pakai \n
print("Ini baris pertama.\nIni baris ke dua.")   # LF -> line Feed
print("Ini baris pertama.\rIni baris ke dua.")   # CR -> Carriage Return
print("Ini baris pertama.\r\nIni baris ke dua.") # CRLF -> Line Feed Carriage Return

# Menggunakan literal dan raw

# Cara pakai \,' agar semua jadi string pakai raw string 
print(r"Ini pakai raw \n \r '''''")

# Menggunakan multi line literal string
print('''
Nama  : Budi
Kelas : 6SD\new era
''')

# Menggunakan multi line literal string and RAW
print(r'''
Nama  : Budi
Kelas : 6SD\new era
''')