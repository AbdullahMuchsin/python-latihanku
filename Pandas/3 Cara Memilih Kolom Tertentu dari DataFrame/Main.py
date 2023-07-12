import pandas as pd

# Cara memilih data tertentu dari DataFrame
data = pd.read_csv("data_csv.csv")
print(data)
print("============================ data[x] ambil data yang di inginkan ")
hasil0 = data["age"]
print(type(hasil0))
print(hasil0.tail(7))
print("============================ data[[x,x]] ambil dari dari 1 kolom")
hasil1 = data[['sex','age']] # Kalau mau pilih dari 1 data jangan lupa dijadikan 2D
print(type(hasil1))
print(hasil1.head(12))
print("============================ data[x] > x ambil data yang dengan ekspresi")
hasil21 = data["age"] < 20
hasil22 = data[data["age"] < 20]
print(hasil21)
print(hasil22)
print(hasil22.shape)
print("============================ data[(data['pclass'] == 2) | (data['pclass'] == 3)] sama dengan itu hanya penulisan berbeda")
hasil31 = data["pclass"].isin([2,3])
hasil32 = data[data["pclass"].isin([2,3])]
print(hasil31)
print(hasil32)
print("============================ sama dengan fungsi isin()")
hasil41 = (data["pclass"] == 2) | (data["pclass"] == 3)
hasil42 = data[(data["pclass"] == 2) | (data["pclass"] == 3)]
print(hasil41)
print(hasil42)
print("============================ Mengambil nilai age yang bukan null")
hasil51 = data["age"].notna()
hasil52 = data[data["age"].notna()]
print(hasil51)
print(hasil52)
print("============================ Memilih dengan ekspresi dengan kompleks")
hasil6 = data.loc[data["age"] < 25, ["deck","sex"]]
print(hasil6)
print("============================ parameter 1 memilih baris parameter 2 memilih kolom")
hasil7 = data.iloc[4:20, 1:4]
print(hasil7)
print("============================ parameter 1 memilih baris parameter 2 memilih kolom dan di ikuti dengan ekspresi")
hasil8 = data.iloc[1:10, 2] == "female"
print(hasil8)