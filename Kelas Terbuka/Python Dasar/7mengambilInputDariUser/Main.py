# BELAJAR INPUT DARI USER

# type data input = str
data = input("Masukkan data : ")
print("Data =", data, "Type :", type(data))

# Casting input 
## INTEGER and FLOAT
number = int(input("Masukkan number : "))
# number = float(input("Masukkan angka : "))

print("number =", number, "Type :", type(number))

## BOOLEAN
data_bool = bool(float(input("Masukkan angka : ")))
print("data_bool =", data_bool, "Type :", type(data_bool))

## COMPLEX
# data_com = complex(input("Masukan data complex ="))
# print("data_com =", data_com, "Type :", type(data_com))
