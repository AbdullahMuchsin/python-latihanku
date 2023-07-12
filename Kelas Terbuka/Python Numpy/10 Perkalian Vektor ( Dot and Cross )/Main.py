import numpy as np

a1 = np.array([1,2]) # x , y
b1 = np.array([4,1]) # x , y

print("Perkalian Vektor Dot:")
c = np.dot(a1,b1)
print(c)

print("perkalian Vektor Cross:")
a2 = np.array([5,1,0]) # x , y, z
b2 = np.array([1,4,0]) # x , y, z

c21 = np.cross(a2,b2)
c22 = np.cross(b2,a2) 

print(c21)
print(c22)
