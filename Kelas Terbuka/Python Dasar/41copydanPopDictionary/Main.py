## BELAJAR COPY AND POP DICTIONARY

# Copy
sayuran = {
    "tom":"Tomat",
    "lom":'Lombok',
    'ter':"Terong",
    'wor':'Wortel'
}

csayur = sayuran.copy()
print(f"Sayuran : {sayuran}")
print(f"Copy Sayuran : {csayur}\n")

sayuran['lom'] = "Lobak"

print(f"Sayuran : {sayuran}")
print(f"Copy Sayuran : {csayur}\n")

# Pop dictionaray
pcs = csayur.pop('tom') # Di ambil value 
print(f"Sayuran : {pcs}")
print(f"Copy Sayuran : {csayur}\n")

# Popitem dictionary
pis = sayuran.popitem({'tom':'tomat'}) # Di ambil keys and values yang terakhir
print(f"Sayuran : {pis}")
print(f"Copy Sayuran : {sayuran}\n")