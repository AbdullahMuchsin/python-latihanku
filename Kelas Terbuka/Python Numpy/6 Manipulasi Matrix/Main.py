import numpy as np

if __name__ == "__main__":
    a = np.array([[1,2,3,4],
                  [0,1,3,2]])
    
    print("Matrix a adalah ({})".format(a.shape))
    print(a)

    # Transpose Matrix
    print("Transpose Matrix dari a:")
    print(np.transpose(a))
    print(a.transpose())
    print(a.T)

    # Flatten Array, Vector Baris
    print("Flutten Array / Vector Baris (ravel) dari Matrix a:")
    print(np.ravel(a))
    print(a.ravel())

    # Reshape Matrix
    print("Reshape Matrix dari Matrix a :")
    print(np.reshape(a,(1,8)))
    print(a.reshape(4,2))

    # Resize Matrix
    print("Matrix a adalah ({})".format(a.shape))
    print("Resize Matrix dari Matrix a:")
    a.resize(8,1) # Menggunakan resize matrix tidak mengembalikan nilai
    print(a)
    print("Matrix a adalah ({})".format(a.shape))

    # Resize Matrix
    print("Resize Matrix dari Matrix a:")
    print(np.resize(a,(4,2))) # Menggunakan resize matrix dengan mengembalikan nilai
    print("Matrix a adalah ({})".format(a.shape))

