import numpy as np

# Mencari index dengan nilai yang diketahui dengan fungsi where
a = np.array([1,2,3,4,5,6,7])
_a = np.array([2,4,6,7])
a_ = np.array([8,23,2,1,6,3,1])

print("==============1")
x = np.where(a == 4)
print(x)
print('==============2')
# Mencari Genap
x = np.where(a%2 == 0)
print(x)
print('==============3')
# Mencari ganjil
x = np.where(a%2 == 1)
print(x)

# Pakai fungsi searchsorted Mencari index dengan nilai yang diurutkan
print('==============4')
x = np.searchsorted(_a, 4)
print(x)

print('==============5')
x = _a.searchsorted(2)
print(x)

print('==============5')
x = np.searchsorted(a_, 6, side="right")
print(x)

print("==============6")
x = np.searchsorted(_a, [1,3,5])
print(x)