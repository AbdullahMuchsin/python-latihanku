import numpy as np

# Cara mencari nilai dengan parameter radian
print("=================== SIN")
hasil = np.sin(np.pi/2)
print(hasil)
hasil = np.sin([np.pi/2,np.pi/3,np.pi/4]) # list / array
print(hasil)
print("=================== COS")
hasil1 = np.cos(np.pi/2)
print(hasil1)
hasil1 = np.cos([np.pi/2,np.pi/3,np.pi/4]) # list / array
print(hasil1)
print("=================== TAN")
hasil2 = np.tan(np.pi/2)
print(hasil2)
hasil2 = np.tan([np.pi/2,np.pi/3,np.pi/4]) # list / array
print(hasil2)
# Cara Konveris radian ke besar sudut dengan rad2deg or dag2rad
print("=================== RAD2DEG")
hasil3 = np.rad2deg(np.pi/2)
print(hasil3)
hasil3 = np.rad2deg([np.pi/2,np.pi/3,np.pi/4])
print(hasil3)
print("=================== DEG2RAD")
hasil4 = np.deg2rad(90)
print(hasil4)
hasil4 = np.deg2rad([90, 60, 45])
print(hasil4)
# Cara konversi hasil ke radian dengan arcsin, arccos, dan arctan
print("=================== ARCSIN")
hasil5 = np.arcsin(1.0)
print(hasil5)
hasil5 = np.arcsin([1.0,0.8660254,0.70710678])
print(hasil5)
print("=================== ARCCOS")
hasil6 = np.arccos(6.123233995736766e-17)
print(hasil6)
hasil6 = np.arccos([6.12323400e-17,5.00000000e-01,7.07106781e-01])
print(hasil6)
print("=================== ARCTAN")
hasil7 = np.arctan(1.633123935319537e+16)
print(hasil7)
hasil7 = np.arctan([1.63312394e+16,1.73205081e+00,1.00000000e+00])
print(hasil7)
# cara menemukan hasil dari panjang dan lebar dari teorema pythagoras
print("=================== HYPOT")
alas = 6
tinggi = 8
hasil8 = np.hypot(alas,tinggi)
print(hasil8)