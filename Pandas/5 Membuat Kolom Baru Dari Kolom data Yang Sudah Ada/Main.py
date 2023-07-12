import pandas as pd

df = pd.read_csv('data.csv', index_col=0, parse_dates=True)
# Cara nambah kolom atau data baru seperti di dictionary
df["tanggal"] = df["kelas"] * 2
print("================================== DF NORMAL")
print(df)
df_renamed1 = df.rename(
    columns={
        "nama" : "NAMA",
        "umur" : "UMUR"
    })
df_renamed2 = df.rename(columns=str.upper)
print("================================== DF Rename 1")
print(df_renamed1)
print("================================== DF Rename 2")
print(df_renamed2)
