import numpy as np

x = np.array([10,2,-23,4,5,33])

# fungsi diff di numpy berguna untuk operasi mengurangi antar n
print("===================== DIFF")
# 1 + -2 + 3 = (-2-1) + (3-(-2)) = [-2 5]
hasil = np.diff(x)
print(hasil)
# dengan parameter n untuk berapa pengulangan yang di ingin kan
hasil2 = np.diff(x, n=2)
print(hasil2)