# Menggunakan modul dengan form alias

import aritmatika as math # Alias atau as berfungsi mengganti nama modul
from aritmatika import tambah as add, kurang as minus

print(add(2,25,25,63,61,46)) # Dengan from
print(minus(2,25,25,63,61,46))
print(math.kali(2,25,25,63,61,4)) # Tanpa From
print(math.pangkat(2)(5))
