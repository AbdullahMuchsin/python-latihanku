import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])

x1 = np.array([[1,2,3,4],[5,6,7,8]])
y1 = np.array([[12,11,14,16],[22,23,21,32]])

# Bergabung dengan fungsi concatenate
xy1 = np.concatenate((x,y))
xy2 = np.concatenate((x1,y1), axis = 1) 
print("1")
print(xy1)
print("2")
print(xy2)

# Bergabung dengan fungsi stack
xy3 = np.stack((x1,y1), axis = 2)
print("3")
print(xy3)

# Begabung secara horizontal
xy4 = np.hstack((x1,y1))
print("4")
print(xy4)

# Bergaung secara vertika
xy5 = np.vstack((x1,y1))
print("5")
print(xy5)

# bergabung dengan ketinggian dan lebar yang sama
xy6 =np.dstack((x1,y1))
print("6")
print(xy6)