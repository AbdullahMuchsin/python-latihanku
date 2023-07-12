trying = 0
misetry = 6
limit = 3

while trying < limit:
    guess_number = int(input("Masukan angka tebakan (1-9) : "))

    if guess_number == misetry:
        print("Selamat kamu menang !!!")
        break
    trying += 1
    if trying == 3:
        print("Anda gagal menebak")
