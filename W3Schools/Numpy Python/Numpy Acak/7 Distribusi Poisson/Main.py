import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Dsitribusi Poisson adalah berapa kemungkinan terjadi di kejadian tertentu misal
# Ada dua parameter lam letak kejadian size berapa percobaan yang ingin di hasilkan
x = random.poisson(lam=5, size=(1000))
print(x)

plt.figure("Poisson 1")
sns.distplot(x, kde=True, hist=True, label="Poisson 1")

# Perbandingan distribusi normal dengan poisson
plt.figure("Perbandingan poisson dengan normal")
sns.distplot(random.poisson(lam=50,size=(1000)), hist=False)
sns.distplot(random.normal(loc=50, scale=7, size=(1000)), hist=False)

# Perbandingan distribusi poisson dengan binomial
plt.figure("Perbandingan distribusi poisson dengan binomial")
sns.distplot(random.poisson(lam=10, size=1000), hist=False)
sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False)
plt.show()