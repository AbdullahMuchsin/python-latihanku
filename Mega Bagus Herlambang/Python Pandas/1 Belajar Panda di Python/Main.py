import pandas as pd

print("================== Cara baca file di pandas dengan read_namaFileNya")
kapal = pd.read_csv('kapal_titanic.csv')
print("================== Fungsi head pandas berguna untuk cetak lima list pertama")
print(kapal.head())
print("================== Fungsi tail pandas berguna untuk cetak lima list terakhir")
print(kapal.tail())
print("================== cara koversi file di panda denfan fungsi to_namaFile")
kapal.to_excel('data_excel.xlsx',index=False, sheet_name="sheet1")
kapal2 = pd.read_excel('data_excel.xlsx', sheet_name="sheet1")
print(kapal2)