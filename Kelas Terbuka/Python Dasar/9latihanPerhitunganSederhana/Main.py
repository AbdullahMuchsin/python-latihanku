# LATIHAN PERTAMA
## MEMBUATA KONVERSI TEMPERATUR

# Celcius
celcius_ = float(input('Masukan suhu celcius :'))
print("Suhu celcius adalah",celcius_,"Celcius")
## KONVERSI
# Rahrenheit
reamur1 = (4/5) * celcius_
print("Suhu reamur adalah",reamur1,"Reamur")
# Fahrenheit
fahrenheit1 = ((9/5) * celcius_) + 32
print("Suhu fahrenheit adalah",fahrenheit1,"Celcius")
# Kelvin
kelvin1 = celcius_ + 273
print("Suhu kelvin adalah",kelvin1,"Celcius")

## PR become for fahrenheit to kelvin and in contrast
# Fahrenheit to Kelvin
fahrenheit_ = float(input('\nMasukan suhu fahrenheit:'))
print("Suhu fahrenheit adalah",fahrenheit_,"Fahrenheit")
celcius_1 = (5/9 * (fahrenheit_ - 32))
kelvin2 = celcius_1 + 273
print("Suhu kelvin adalah",kelvin2,"Kelvin")

# Kelvin to Fahrenheit
kelvin_ = float(input('\nMasukan suhu kelvin :'))
print("Suhu kelvin adalah",kelvin_,"kelvin")
celcius_2 = kelvin_ - 273
fahrenheit2 = ((9/5) * celcius_2) + 32
print("Suhu fahrenheit adalah",fahrenheit2,"Fahrenheit")