import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Cara mengimplementasikan data dsistribusi di kurva dengan modul matplotlib dan seaborn
plt.figure("Dengan Kurva Histogram")
x = np.arange(10)
y = x * 2 + 3
sns.distplot(y)

plt.figure("Tanpa Kurva Histogram")
sns.distplot([2,2,3,4,2,6,7], hist=False)

plt.show()