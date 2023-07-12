import numpy as np

list_biasa = [1,2,3,4,5]
list_numpy = np.array([1,2,3,4,5])

# list_biasa **= 2 Tidak bisa
print(f"list biasa : {list_biasa}")

list_numpy **= 2
print(f"list numpy : {list_numpy}")

matrix_a = np.array([1,2])
print(f"matrix a : {matrix_a}")

matrix_b = np.array([(1,2),(1,2)])
print(f"matrix b : \n{matrix_b}")

matrix_c, matrix_d = matrix_a*2, matrix_b**2
print(f"matrix c : {matrix_c}")
print(f"matrix d : \n{matrix_d}")

ones_e = np.ones((3,2)) # baris 3 kolom 2
print(f"isi matrix 1 :{ones_e}")

zeros_f = np.zeros((2,3)) # baris 2 kolom 3
print(f"isi matrix 0 :{zeros_f}")

# Latihan membuat matrik perkalian

matrix_a = np.array([(5,6),(2,7)])
matrix_b = np.array([[1,4],[4,5]])

kali_matrix = matrix_a * matrix_b

print(f'\n{"PERKALIAN MATRIX":^20}')
print("-"*20)

print(f"Matri a : \n {matrix_a}")
print(f"Matri b : \n {matrix_b}")
print(f"Matrix a x Matrix b : \n {matrix_a}\n x \n {matrix_b} \n adalah : \n {kali_matrix}")
