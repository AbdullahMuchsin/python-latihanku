## BELAJAR LIST BERSARANG (LIST 2D)

# List 2D
p1 = ["Surudin",17,"Laki-Laki"]
p2 = ["Denis",18,"Wanita","Memasak"]
p3 = ["Mamat",14,"Laki-Laki","Coding"]
p4 = ["Niko",24,"Laki-Laki"]


pk = [p1,p2,p4,p3]
print(pk)

for p in pk:
    pl = len(p)
    print(f"Nama     : {p[0]}")
    print(f"Umur     : {p[1]}")
    print(f"Gander   : {p[2]}")
    if pl == 3:
        print(" ")
    elif pl > 3:
        print(f"Keahlian : p{3}\n")

# Jika duplikat pakai copy maka hanya bagian terluar saja
pcopy = pk.copy()
print(str(pcopy) + "\n")
p4[0] = "Musdin"
## Sama-sama berubah
print(str(pcopy) + "\n")
print(str(pk) + "\n")
