numbers = (1,4,6,1,3)

print("Belajar unpack")

a = numbers[3]
print(a)

a,b,c,d,e = numbers # Jumblah variable dengan jumblah item list harus sama
print(a,b,c,d,e)

numbers1 = (1,4,6,1,3)

x,y,_,z,_ = numbers1 # Pakai tanda _ artinya variable yang tidak memiliki nilai
print(x,y,z)

numbers2 = (1,4,6,1,3)

p,_,*q = numbers2 # Pakai tanda * Nilai item list berikutnya di tampung di dalam variable yang ada tanda *
print(p)
print(q)