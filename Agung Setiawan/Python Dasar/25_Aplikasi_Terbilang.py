numbers = input("Masukan angka : ")

number_mapping = {
    "0" : "Nol",
    "1" : "Satu",
    "2" : "Dua",
    "3" : "Tiga",
    "4" : "Empat",
    "5" : "Lima",
    "6" : "Enam",
    "7" : "Tuju",
    "8" : "Delapan",
    "9" : "Sembilan"
}

hasil = ""

for number in numbers:
    terbilang = number_mapping.get(number,"error")
    hasil = hasil + terbilang + " "

print(hasil)