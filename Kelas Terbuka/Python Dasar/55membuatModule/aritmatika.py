# Ini Modul

def tambah(*args):
    hasil = 0
    for i in args:
        hasil += i

    return hasil

def kurang(*args):
    hasil = 1000
    for i in args:
        hasil -= i

    return hasil

def kali(*args):
    hasil = 1
    for args in args:
        hasil *= args

    return hasil

def pangkat(n):
    return lambda hasil:hasil**n
