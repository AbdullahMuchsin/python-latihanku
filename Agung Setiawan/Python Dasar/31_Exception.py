try:
    hasil = int(input("Masukan angka : "))
    hasil = hasil / 0
except ZeroDivisionError:
    print("error di bagi 0")
except ValueError:
    print("Yang anda masukan bukan angka")
except EOFError:
    print("char error")
