# BELAJAR MEMBUAT PACKAGE SEDERHANA
import time

start_time = time.time()


import dataDiri.fulan # Normal
from dataDiri import fulan # Dengan from
from dataDiri.fulan import data_diri # Dengan from tapi package dan modul di sambung
import dataDiri.fulan as dataFulan # Di kasih alias 
from dataDiri.fulan import data_diri as dataSurudin # Sama dengan baris ke 3 tapi ini dikasih alias


dataDiri.fulan.data_diri(nama = "Fulan", umur = 17, status = "Belum Menikah")
fulan.data_diri(nama = "Surudin", umur = 19, status = "Belum Menikah")
data_diri(nama = "Fulan", umur = 17, status = "Belum Menikah")
dataFulan.data_diri(nama = "Fulan", umur = 17, status = "Belum Menikah")
dataSurudin(nama = "Surudin", umur = 19, status = "Belum Menikah")

end_time = time.time()
selisih = (end_time - start_time)
print(selisih)


