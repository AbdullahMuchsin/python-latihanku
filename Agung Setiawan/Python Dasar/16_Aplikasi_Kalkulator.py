# (+ - * /)
command = ""

while command != "Exit" or command != "exit":
    command = input("Masukan operator (+ - * /) : ")

    if command == "Exit" or command == "exit":
        break

    if command != "+" and command != "-" and command != "*" and command != "/":
        print("Maaf operator tidak dikenali")
        continue
    
    angka1 = int(input("Masukan angka pertama : "))
    angka2 = int(input("Masukan angka kedua   : "))

    if command == "+":
        hasil = angka1 + angka2
    if command == "-":
        hasil = angka1 - angka2
    if command == "*":
        hasil = angka1 * angka2
    if command == "/":
        hasil = angka1 / angka2

    print(f"Hasil nya adalah : {hasil}")

print("Terima kasih telah menggunkan aplikasi kami")