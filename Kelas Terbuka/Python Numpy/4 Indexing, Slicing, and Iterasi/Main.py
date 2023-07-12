import numpy as np

if __name__ == '__main__':
    ndarray = np.arange(10)**2
    
    # Mengambil data
    print("urutan ke - 1 =",ndarray[0])
    print("urutan ke - 6 =",ndarray[5])
    print("urutan ke - 10 =",ndarray[-1])

    # Slicing
    print("urutan ke - 4:8 =",ndarray[3:8])
    print("urutan ke - 1:4 =",ndarray[0:5])
    print("urutan ke - 1:8 =",ndarray[:8])
    print("urutan ke - 5:end =",ndarray[4:])
    print("urutan ke - start:end =",ndarray[:])

    # Iterasi
    for index,data in enumerate(ndarray):
        print("index ke - {} adalah {}".format(index + 1,data))