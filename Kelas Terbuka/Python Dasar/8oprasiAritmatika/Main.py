# BELAJAR ARITMATIKA

a = 5
b = 2

## Aritmatika penjumblahan +
hasil = a + b
print('a','+','b','=',hasil)

## Aritmatika pengurangan -
hasil = a - b
print('a','-','b','=',hasil)

## Aritmatika perkalian *
hasil = a * b
print('a','*','b','=',hasil)

## Aritmatika pembagian /
hasil = a / b
print('a','/','b','=',hasil)

## Aritmatika modulus(sisa pembagian) %
hasil = a % b
print('a','%','b','=',hasil)

## Aritmatika floor division(dibulatkan kebawah) //
hasil = a // b
print('a','//','b','=',hasil)

## Aritmatika eksponen(perpangkatan) **
hasil = a ** b
print('a','**','b','=',hasil)

## PRIORITAS ARITMATIKA
'''
    1. Yang di kurung ()
    2. Eksponen **
    3. Perkalian dan kawan kawan *,/,%,//
    4. Pengurangan dan Penjumblahan
'''

# EXAMPLE
A = 5
b = 3
c = 2

hasil = a + b ** c / a % (a - b) // c + a - b / b
print('a','+','b','**','c','/','a','%',"(a - b)","//",'c','+','a','-','b','/','b','=',hasil)

hasil = (a + b) * c
print('(a + b)','*','c','=',hasil)

hasil = (a + b) // c
print('(a + b)','//','c','=',hasil)
