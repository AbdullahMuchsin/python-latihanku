import numpy as np

a = np.array([2,3,1,2,4,342,35,13,55,3,53,53,2])
a1 = np.array(["Domba","Kuda","Singa"])
a2 = np.array([True,False,True,False])

b = np.array([[2,3,41,3],
              [3,5,32,3]])

# Cara mengurutkan array dapat dengan fungsi sort
# Jika yang di sort 2D maka mengurutkanya baris per baris

print(np.sort(a))
print("=============================")
print(np.sort(a1))
print("=============================")
print(np.sort(a2))
print("=============================")
print(np.sort(b))
print("=============================")
