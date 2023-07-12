message = input("Masukan kalimat : ")

emoji_mappings = {
    ":)" : "(●'◡'●)",
    ":D" : "╰(*°▽°*)╯",
    ":(" : "(┬┬﹏┬┬)",
    ":|" : "(⌐■_■)",
    ":v" : "(^///^)"
}
kalimat = message.split(" ")
print(kalimat)
hasil = ""
for k in kalimat:
    hasil = hasil + emoji_mappings.get(k,k) + " "

print(hasil)