''' Data diri milik si Fulan '''

def data_diri(**kwargs):
    NAMA = kwargs["nama"]
    UMUR = kwargs["umur"]
    STATUS = kwargs["status"]

    print(f'''
    Nama   : {NAMA}
    Umur   : {UMUR}
    Status : {STATUS}
    ''')