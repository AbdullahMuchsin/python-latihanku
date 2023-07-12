import numpy as np

# Cara milih nilai dengan probabilitas tertentu dengan fungsi choice
x = np.random.choice([1,2,3,4,5], p=[0.2,0.1,0.3,0.4,0.0], size=(10)) # Menghasilkan 10 kolom karna size
print(x)

x = np.random.choice([1,2,3,4,5], p=[0.2,0.1,0.3,0.4,0.0], size=(4,5))
print(x)