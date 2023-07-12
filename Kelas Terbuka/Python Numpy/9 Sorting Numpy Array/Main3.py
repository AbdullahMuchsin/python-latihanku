import numpy as np

dtipe = [('nama','S15'),('tinggi',int)]
data = [
    ('Muchsin',185),
    ('Irma',180),
    ('Dewi',190)
]

a = np.array(data, dtype = dtipe)
print(a)
print('Mengurutkan Array a:')
print(np.sort(a, order=['tinggi']))
print(np.sort(a, order=['nama']))
print(np.sort(a, order=['tinggi','nama']))