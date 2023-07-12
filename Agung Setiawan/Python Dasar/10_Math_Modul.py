import math

number = 7.3
number2 = 7.8

# round fungsi berfungsi membulatkan ke atas or ke bawah
print(round(number))
print(round(number2))

number3 = 3.1
number4 = 3.9

# Untuk pakai fungsi matematika yang lebih banyak bisa import modul math
# Contohnya ceil dan floor dan masih banyak lagi
print(math.ceil(number3)) # ceil fungsi berfungsi memaksa membulatkan ke atas
print(math.floor(number4)) # floor fungsi berfungsi memaksa membulatkan ke bawah

sin90 = 90
print(math.sin(math.radians(90))) # Untuk mengubah ke sin dari besar sudut misal dari contoh tersebut
# 90 derajat pakai radians biar terubah jadi radians

pi = math.pi # pi variable Untuk pakai perhitungan pi 3,14
print(pi*2)
