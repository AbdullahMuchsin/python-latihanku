import numpy as np

# Membuat Vektor dengan Array Numpay
a = np.array([1,2,3,4,5,6,7])
b = np.array([1,2.5,3,5])

# Membuat Vektor dengan range
c = np.arange(1,10)
d = np.arange(1,10,2)

# Membuat Vektor dengan linespace
e = np.linspace(1,10,3)

# Array Multidimensi/Matrix
f = np.array([(1,2,3,4,5) , (6,7,8,9,10)])

# Matrix dengan nilai nol
g = np.zeros((5,5))

# Matrix dengan nilai sat
h = np.ones((5,7))

# Matrix identitass
i = np.identity(5) # identity dengan eye sama hasilnya
j = np.eye(4)


# Display
print("="*10)
print(a)
print("="*10)
print(b)
print("="*10)
print(c)
print("="*10)
print(d)
print("="*10)
print(e)
print("="*10)
print(f)
print("="*10)
print(g)
print("="*10)
print(h)
print("="*10)
print(i)
print("="*10)
print(j)
print("="*10)