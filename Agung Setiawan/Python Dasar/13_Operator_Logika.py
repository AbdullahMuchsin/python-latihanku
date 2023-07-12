name = "Abdullah Muchsin"
by_pass_validation = True
'''
    or jika salah satu True maka hasilnya True
    and jika salah satu salah maka hasilnya False jika True harus semua bernilai True
    ^ jika bernilai sama maka false dan sebaliknya
    not maka akan membalikkan nilai misal True menjadi False
'''
if (len(name) > 5) ^ (by_pass_validation):
    print(f"walcome {name}")
else:
    print("Maaf nama tidak memenuhi kondisi")