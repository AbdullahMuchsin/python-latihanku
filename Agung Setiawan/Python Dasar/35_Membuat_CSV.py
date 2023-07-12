import csv
file = open("Database/data_2.csv", mode="r")

read_csv = csv.reader(file, delimiter=",")

for index, data in enumerate(read_csv):
    print(f"{index + 1}. Name : {data[0]}, Username : {data[1]}, Role : {data[2]}")

file.close()