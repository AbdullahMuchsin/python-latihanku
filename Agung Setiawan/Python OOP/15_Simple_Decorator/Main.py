def info(path):
    def view():
        print("*"*10)
        path()
        print("*"*10)

    return view

def say_hello():
    print("Hai Dunia Saya Belajar Bahasa Python")

view = info(say_hello)
view()
