import numpy as np

# Cara buat angka acak bilangan bulat dengan randint dan rand untuk biangan desimal
# Bilangan bulat
print("============== RANDOM INTEGER ==================")
ex = np.random.randint(20, size = 5)
print(ex)
x = np.random.randint(100)
print(x)
x = np.random.randint(50, size = (5)) # Ambil 5 nilai kolom
print(x)
x = np.random.randint(40,90, size = (4,6)) # Ambil 4 baris dan ada 6 kolom dan nilai antara 40 - 90
print(x)

# Bilangan random desimal
print("============== RANDOM DESIMAL ==================")
x = np.random.rand()
print(x)
x = np.random.rand(5) # Ambil 5 nilai kolom
print(x)
x = np.random.rand(4,6) # Ambil 4 baris dan ada 6 kolom dan nilai antara 40 - 90
print(x)

# Cara ambil nilai acak dari array atau nilai yang sudah ada
print("============== RANDOM CHOICE ==================")
x = np.random.choice([1,2,3,4,5])
print(x)
x = np.random.choice(ex, size = (9)) # Ambil 9 nilai kolom dari array ex
print(x)
x = np.random.choice(ex, size = (5,6)) # Ambil 5 baris dan ada 6 kolom dan nilai dari array ex
print(x)