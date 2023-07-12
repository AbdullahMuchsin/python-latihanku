import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.binomial(n=100, p=0.5, size=(1000))
print(x)
y = random.normal(loc = 50, scale=5, size = (1000))
print(y)
sns.distplot(x,kde=True, hist=False, label="Pertama")
sns.distplot(y,kde=True, hist=False, label="Kedua")
plt.show()