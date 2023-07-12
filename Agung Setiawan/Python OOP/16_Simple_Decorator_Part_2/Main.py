def info(path):
    def view():
        print("*"*10)
        path()
        print("*"*10)

    return view

@info
def say_hello():
    print("Hai Dunia Saya Belajar Bahasa Python")

say_hello()
