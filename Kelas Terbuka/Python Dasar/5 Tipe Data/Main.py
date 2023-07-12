print("===TIPE DATA===")

#pertama tipe data integer
tipe_integer = 10
print("Tipe data integer ", tipe_integer)
print("class ", type(tipe_integer))

#kedua tipe data float
tipe_float = 10.8
print("Tipe data float ", tipe_float)
print("class ", type(tipe_float))

#ketiga tipe data string
tipe_string = "Ini adalah string"
print("Tipe data ", tipe_string)
print("class ", type(tipe_string))

#keempat tipe data bool
tipe_bool = True
print("Tipe data bool ", tipe_bool)
print("class ", type(tipe_bool))

#tipe data kompleks
tipe_complex = complex(5,8)
print("Tipe data complex ", tipe_complex)
print("class ", type(tipe_complex))

#cara import tipe data dari bahasa c
from ctypes import c_double, c_long

tipe_double = c_double(82.323)
print("Tipe data double ", tipe_double)
print("class ", type(tipe_double))

tipe_long = c_long(46235473)
print("Tipe data long ", tipe_long)
print("class ", type(tipe_long))