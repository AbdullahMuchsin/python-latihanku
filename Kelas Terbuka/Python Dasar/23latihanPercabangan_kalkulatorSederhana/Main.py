# LATIHAN MEMBUAT KALKULATOR SEDERHANA

print("="*20)
print("kalkulator sederhana".upper())
print("="*20,"\n")

print("""1. Operator Pertambahan (+)
2. Operator Pengurangan (-)
3. Operator Perkalian (x)
4. Operator Pembagian (/)
5. Operator Modulus (%)
6. Operator Floor Division (//)
7. Operator Eksponen (**)\n
""")
operator = int(input("Pilih operator yang akan digunakan : "))

if operator == 1:
    angka1 = float(input("Masukan angka 1 : "))
    angka2 = float(input("Masukan angka 2 : "))
    hasil = (angka1 + angka2)
    print(f"Hasil dari {angka1} + {angka2} adalah = {hasil}")
elif operator == 2:
    angka1 = float(input("Masukan angka 1 : "))
    angka2 = float(input("Masukan angka 2 : "))
    hasil = (angka1 - angka2)
    print(f"Hasil dari {angka1} - {angka2} adalah = {hasil}")
elif operator == 3:
    angka1 = float(input("Masukan angka 1 : "))
    angka2 = float(input("Masukan angka 2 : "))
    hasil = (angka1 * angka2)
    print(f"Hasil dari {angka1} x {angka2} adalah = {hasil}")
elif operator == 4:
    angka1 = float(input("Masukan angka 1 : "))
    angka2 = float(input("Masukan angka 2 : "))
    hasil = (angka1 / angka2)
    print(f"Hasil dari {angka1} / {angka2} adalah = {hasil}")
elif operator == 5:
    angka1 = float(input("Masukan angka 1 : "))
    angka2 = float(input("Masukan angka 2 : "))
    hasil = (angka1 % angka2)
    print(f"Hasil dari {angka1} % {angka2} adalah = {hasil}")
elif operator == 6:
    angka1 = float(input("Masukan angka 1 : "))
    angka2 = float(input("Masukan angka 2 : "))
    hasil = (angka1 // angka2)
    print(f"Hasil dari {angka1} // {angka2} adalah = {hasil}")
elif operator == 7:
    angka1 = float(input("Masukan angka 1 : "))
    angka2 = float(input("Masukan angka 2 : "))
    hasil = (angka1 ** angka2)
    print(f"Hasil dari {angka1} ** {angka2} adalah = {hasil}")
else:
    print("\nOperator yang anda pilih salah!")

print("\n" + "="*5 + "akhir dari program".upper() + "="*5)
