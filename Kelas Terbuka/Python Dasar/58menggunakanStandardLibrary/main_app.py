## BELAJAR MENGGUNAKN STANDARD LIBRARY

# MENGGUNAKAN LIBRARY WAKTU YAITU DATETIME
import datetime

data_waktu = datetime.datetime.now()
print(f"Waktu all = {data_waktu}")
print(f"Waktu hari = {data_waktu:%A}")
print(f"Seperti tanggal lahir = {data_waktu:%x}")


# Library collections adalah library seperti array list dan kawan kawan 
# Untuk Counter digunakan untuk menghitung agar lebih efisien
from collections import Counter

data = ['2','4','2','4','2','5','2','5','2','2']
dict_data = Counter(data)
print(f"{dict_data}")
print(f"{dict_data['2']}")

import io

dataRead = io.open("58menggunakanStandardLibrary/main_text.txt","r") # ini membukan file main_text.txt r itu memberi perintah membaca
print(dataRead.read())

import calendar

data_calen = calendar.calendar(0)
print(data_calen)