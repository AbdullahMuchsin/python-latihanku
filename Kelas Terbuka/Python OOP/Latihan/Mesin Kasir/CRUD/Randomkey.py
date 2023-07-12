import random, string
def random_key(panjang):
    kunci = "".join(random.choice(string.ascii_letters) for i in range(panjang))
    return kunci