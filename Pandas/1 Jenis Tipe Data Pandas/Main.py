import pandas as pd

df = pd.DataFrame(
    {
        "Nama" : ["Muchsin", "Irma", "Nabila"],
        "Umur" : [28,22,16],
        "Gender" : ["Pria", "Wanita", "Wanita"]
    }
)
print("===================== DataFrame")
print(df)
print("Nilai max :", df["Umur"].max())
print("Nilai min :", df["Nama"].min())
srs = pd.Series(["MA","MTS","SD"], name="kelas")
print("===================== Series")
print(srs)
print("Nilai max :", srs.max())
print("Nilai min :", srs.min())
print("===================== Describe")
print(df.describe())
print("---------------------")
print(srs.describe())