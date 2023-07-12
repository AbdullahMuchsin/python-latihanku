import numpy as np

if __name__ == '__main__':
    
    # Membuat Matrix Dangan Tipe Data Tertentu
    a = np.array([[1,2,3,4],[5,6,7,8]], dtype = float)
    print(a)

    # Membuat Array Dengan Menggunakan Function
    def kuadrat(baris,kolom):
        return baris - kolom
    def tambah (baris,kolom):
        return (baris + kolom)
    
    b = np.fromfunction(kuadrat, (3,3), dtype = int)
    d = np.fromfunction(tambah, (5,5), dtype = int)

    print(b)
    print(d)

    # Multitype Array
    
    iterable = [('nama','S255'),('tinggi',int)]
    data = [
        ('Muchsin', 185),
        ('Irma', 180),
        ('Dewi', 170)
    ]
    e = np.array(data, dtype = iterable)
    print(e[0][0], e[1])