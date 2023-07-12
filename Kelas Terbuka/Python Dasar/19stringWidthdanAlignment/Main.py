# BELAJAR STRING WIDTH AND ALIGNMENT

nama = "Surudin marsudin"
kelas = 10
lahir = "indonesia"

stringl = "STRING LANE"
ub = stringl.center(20,"=")
print(ub)
string_l = f"Nama     : {nama}, \nKelas    : {kelas}, \nLahir Di : {lahir}."
print(string_l + "\n")

# Pakai Multilane
stringl = "STRING MULTILANE"
ub = stringl.center(25,"=")
print(ub)
change = f""" Nama = {nama}
Kelas = {kelas}
Lahir = {lahir}
"""
print(change + "\n")

stringl = "STRING MULTILANE"
ub = stringl.center(25,"=")
print(ub)
change = f""" Nama = {nama:>10}
Kelas = {kelas:>10}
Lahir = {lahir:>10}
"""
print(change)



