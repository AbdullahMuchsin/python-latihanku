# BELAJAR ARGS PADA FUNGSI
import string

def list_data(nama,umur,kota:string) -> string:
    data = "nama " + nama + " dan Umur " + str(umur) + " Tinggal dikota " + kota
    return data

variable_data = list_data("Surudin",17,"Medan")
print(variable_data)

def list_data(data):
    copy_data = data.copy()
    nama = copy_data[0]
    umur = copy_data[1]
    kota = copy_data[2]

    data = "nama " + nama + " dan Umur " + str(umur) + " Tinggal dikota " + kota
    return data

data = (["Marsudin",15,"Jakarta"])
print(list_data(data))

def list_args(*args):
    hasil = 0
    for data in args:
        hasil += data
    
    return hasil

variable_args = list_args(1,2,34,423,25) # args tanpa kurung siku
print(variable_args) 


def list_args(*data):
    hasil = 0
    for data in data:
        hasil += data
    
    return hasil

variable_args = list_args(1,3,25) # args tanpa kurung siku
print(variable_args) 