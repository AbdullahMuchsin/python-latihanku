## LATIHAN FORMAT STRING

# 1. Menggunakan format string di string
nama = "Surudin"
kelas = 12
alamat = "Desa Tunas Mudah"
print(f"Nama : {nama}, Kelas : {kelas}, alamat : {alamat}")

# 2. Menggunkan boolean
boolean = True
bil_Kebeneran = f"Bilangan boolean ini bernilai : {boolean}"
print(bil_Kebeneran)

# 3. Menggunkan angka bilangan bulat
bil_bulat = 1000
print(f"Bilangan bulat ribuan : {bil_bulat:06,}")

# 4. Menggunkan decimal
bil_dec = 25.55333
print(f"Bilangan decimal 2 angka : {bil_dec:.2f}")

# 5. Menggunkan leading zero
print(f"Menggunkan leading zero : {bil_dec:06.2f}")

# 5. Menggunakan plus and minus
plus = 2500
minus = -1500
print(f"Bilangan plus : {plus:+}")
print(f"Bilangan minus : {minus:+}")

# 6. Mengubah bentuk decimal ke persen
persen = 0.0450
print(f"Ini bilangan persen : {persen:.2%}")

# 7. Aritmatika di format
angka1 = 150
angka2 = 50
print(f"Angka1 kali dengan angka2 = {angka1*angka2:,}")

# 8. format angka lain (binary, octal, hexadecimal)
angka = 132
ang_bin = bin(angka)
ang_oct = oct(angka)
ang_hex = hex(angka)

print(f"Ini nilai dari binary : {ang_bin}")
print(f"Ini nilai dari octal : {ang_oct}")
print(f"Ini nilai dari hex : {ang_hex}")
