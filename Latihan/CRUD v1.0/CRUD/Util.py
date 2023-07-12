import random,string

def rand(panjang):
    hasil = "".join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasil