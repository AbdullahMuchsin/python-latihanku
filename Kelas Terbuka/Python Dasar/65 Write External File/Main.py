# BELAJAR WRITE EXTERNAL FILE

# 1. Denga Mode Write

with open("text1.txt" ,"w",encoding="utf-8") as file: # kalau w harus ada encoding untuk pakai karakter apa 
    file.write("Ini contoh 1" + "\n")
    file.write("Ini contoh -")

with open("text1.txt" ,"w",encoding="utf-8") as file: # kalau w harus ada encoding untuk pakai karakter apa 
    file.write("Ini contoh 2" + "\n") # Maka akan overwrite
    file.write("Ini contoh -")

# 2. Denga Mode Append

with open("text2.txt","a",encoding="utf-8") as file: # kalau w harus ada encoding untuk pakai karakter apa 
    file.write("Ini contoh 3\n") # Pakai append akan ditambahkan overwrite
    file.write("Ini contoh -\n")

with open("text2.txt","a",encoding="utf-8") as file: # kalau w harus ada encoding untuk pakai karakter apa 
    file.write("Ini contoh 4\n") # Pakai append akan ditambahkan tanpa overwrite
    file.write("Ini contoh -\n")

# 3. Dengan Mode r+

# Sebelum pakai r+ kita buat dulu file nya karna r+ tidak bisa membuat jadi pakai w atau manual untuk membuatnya
with open("text3.txt","w",encoding="utf-8") as file:
    file.write("Ini contoh 5\n") 
    file.write("Ini contoh -\n")

with open("text3.txt","r+",encoding="utf-8") as file:
    data = file.read() # r+ juga bisa untuk di baca(read)
    print(data)

with open("text3.txt","r+",encoding="utf-8") as file:
    file.write("Ini r+ 1") # jika ada teks akan di timpa sesuai panjang text
    # Jika yang ditambah teks nya lebih dari yang ditimpa maka akan menambahkan sendiri panjang teks nya(tidak error)

with open("text3.txt","r+",encoding="utf-8") as file:
    data = file.read() # Hasil timpa
    print(data)

