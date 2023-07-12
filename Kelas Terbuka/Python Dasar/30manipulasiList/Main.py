# LATIHAN MANIPULATIF LIST
print("PROLOG".center(10,"="))
data = ["jeruk", "nanas", "melon"]
print(data)

# 1. Menampilkan data
print("\n1. Menampilkan data")
print(f"Ini adalah data pertama -> {data[0]}")
print(f"Ini adalah data terakhir -> {data[-1]}")
print(f"Ini adalah data ke-2 -> {data[1]}")



# 2. Menghitung data 
print("\n2. Menghitung data")
data_l = len(data)
print(f"Jumblah data sebesar {data_l}")

# 3. Menambahkan data
print("\n3. Menambahkan data")
data.insert(1,"semangka")
print(f"Menambahkan data ke-2 : {data}")

# 4. Menambahkan data paling akhir
print("\n4. Menambahkan data paling akhir")
data.append("leci")
print(f"Menambahkan data paling akhir : {data}")

# 5. Menambahkan list dengan list
print("\n5. Menambahkan list dengan list")
data_new = ["alpukat", "manggis", "pisang"]
data.extend(data_new)
print(f"Ini adalah data yang ditambah dengan list : {data}")

# 6. Mengubah data
print("\n6. Mengubah data")
data[2] = "tomat"
print(f"Data ke-3 di ubah menjadi 'tomat' : {data}")

# 7. Menghapus data
print("\n7. Menghapus data")
data.remove("melon")
print(f"Data melon telah dihapus : {data}")

# 8. Mengapus/Mengambil data paling terakhir
print("\n8. Menghapus/Mengambil data paling terakhir")
print(f"Data terakhir sebelum di ambil : {data}")
print(f"data yang di ambil adalah ini : {data.pop()}")
print(f"Data terakhir telah di ambil : {data}")

# 9. Mengapus/Mengambil data paling terakhir variable
print("\n9. Menghapus/Mengambil data paling terakhir variable")
print(f"Data terakhir sebelum di ambil : {data}")
data_ambil = data.pop()
print(f"data yang di ambil adalah ini : {data_ambil}")
print(f"Data terakhir telah di ambil : {data}")
