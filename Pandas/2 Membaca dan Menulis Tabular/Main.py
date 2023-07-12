import pandas as pd

# Membaca tabular dengan read_x
print("====================== Read_x")
data = pd.read_csv('data_csv.csv')
print(data)
print("====================== Head")
print(data.head(10)) # Baca 10 row dari atas default 5
print("====================== Tail")
print(data.tail(10)) # Baca 10 row dari bawah default 5
print("====================== to_x")
# Untuk konversi tabular ke format file lain
data.to_excel("excel_csv.xlsx",sheet_name="sheet1",index=False)
dataexcel = pd.read_excel("excel_csv.xlsx")
print(dataexcel)
print("====================== Dtypes")
print(data.dtypes)
print("====================== Info")
print(data.info())