import numpy

# Cara Melakukan permutasi acak dengan modul random
# Ada 2 fungsi yakni shuffle dan permutation
arr = numpy.array([1,3,2,1,5])
# Shuffle Membuat perubahan pada array asli
numpy.random.shuffle(arr)
print("===============SHUFFLE")
print(arr)

# permutation tidak membuat perubahan pada array asli
arr = numpy.array([1,3,2,1,5])

tes = numpy.random.permutation(arr)
print("=============PERMUTATION")
print(arr)
print(tes)