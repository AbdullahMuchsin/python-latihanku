file = open("data.txt", mode="r")
data = file.readlines()


for index, data in enumerate(data):
    data_break = data.split(",")

    presskey = data_break[0]
    tanggal = data_break[1]
    penulis = data_break[2]
    nama = data_break[3]
    tahun = int(data_break[4])

    print(f"{index + 1}. {nama} | {penulis} | {tahun}")
