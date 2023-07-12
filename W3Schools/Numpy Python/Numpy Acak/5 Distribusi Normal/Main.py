import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

ex = random.normal(size=(5))
print(ex)
dn = random.normal(size=10000)
sns.distplot(dn, hist=False)
plt.show()
