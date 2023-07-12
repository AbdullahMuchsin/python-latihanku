import numpy as np

# Mengubah bentuk dimensi dan data array dengan fungsi reshape
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a.shape)
print(a.reshape(3,2,2))

print("Cek apa hasil reshape itu view atau copy dengan base")
arr = a.reshape(4,3)
print(arr.base) # Hasilnya view bukan copy / None

print("Menggunkan akhiran - ketika tidak tahu berapa data kolom")
arr = a.reshape(2,2,-1)
print(arr)
print(arr.shape)
