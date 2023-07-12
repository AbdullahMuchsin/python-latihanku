import numpy as np

a = np.floor(np.random.randn(1,7)*10)

print(a)
print("Nilia Array Max a:", a.max())
print("Posisi Array Max a:", a.argmax())
print("Nilai Array Min a:", a.min())
print("posisi Array  Min a:", a.argmin())

print("Mengurutkan Nilai a:")
print(np.sort(a))
print(np.argsort(a))
