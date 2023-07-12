import numpy as np

d1 = np.array([1,2,3,4,5,6,7,8,9])

d2 = np.array([[1,2,3,4],[4,5,6,7],[1,2,3,4],[4,5,6,7]])

d3 = np.array([[[1,2,3,4],[11,22,33,44]],[[12,11,13,14],[4,3,2,1]],[[1,2,3,4],[11,22,33,44]],[[12,11,13,14],[4,3,2,1]]])

print("="*25)
print(d1)
print("="*25)
print(d2)
print("="*25)
print(d3)
print("="*25)

# Cara membagi array dengan array_split dan split
# Jika pakai array_split ketika jummblah split tidak mendukung maka akan otomatis menyesuaikan nya
# Tapi jika dengan split akan error
x = np.array_split(d1,4)
print(x)

x = np.array_split(d2,2)
print(x)
print("="*25)

x = np.array_split(d3,3)
print(x)
print("="*25)

x = np.array_split(d3,2, axis = 1)
print(x)
print("="*25)

# Displit bisa pakai v,h, dan d
x = np.hsplit(d1, 3)
print(x)
print("="*25)
