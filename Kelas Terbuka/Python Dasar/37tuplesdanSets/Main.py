## BELAJAR DATA TUPLES AND SETS

print("1. List")
list_data = [23,24,21,"Danang"] # Memiliki index dan dapat diubah
print(list_data[-2])
list_data.insert(2,"Ketiga")
print(list_data)
# Tuples 
print("\n2. Tuples")
tuples_data = (2,42,4,2,4,"Gilang") # Tidak dapat diubah tapi memiliki index
print(tuples_data[0])
# tuples_data.uppend("Dani") Tidak bisa
print(tuples_data) # Bisa

# Sets
print("\n3. Sets")
sets_data = {2,4,5,42,"Surudin"} # Dapat diubah tapi tidak memiliki index
# print(sets_data[-1]) Tidak bisa
sets_data.remove(4)
print(sets_data)