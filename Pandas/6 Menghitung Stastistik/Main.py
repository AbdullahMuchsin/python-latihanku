import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data_csv.csv')

print("=============== Mencari Mean")
print("=============== Describe (Detail)")
hasil = data.describe()
print(hasil)
print("=============== mean (nilai rata-rata) and median (nilai rata-rata) bisa series or DataFrame")
hasil = data["age"].mean()
print(hasil)
hasil = data[["fare","age"]].skew()
print(hasil)
print("=============== groupby 1")
hasil = data[["survived","fare"]].groupby("survived").mean()
print(hasil)
print("=============== agg")
hasil = data.agg(
    {
        "age" : ["min", "max", "median", "skew"],
        "fare" : ["min", "max", "median", "mean"]
    }
)
print(hasil)
print("=============== groupby 2")
hasil = data.groupby("sex").mean(numeric_only=True)
print(hasil)
print("=============== groupby 3")
hasil = data["pclass"].value_counts()
print(hasil)
hasil = data.groupby(['age','sex'])['fare'].mean()
print(hasil)
hasil = data.groupby('pclass')['pclass'].count()
print(hasil)