mat1 = [[1,2,3],
        [4,5,6]]
mat2 = [[2,3,4],
        [5,6,7]]

# Penjumblahan
for i in range(0,len(mat1)):
    for j in range(0,len(mat1[0])):
        print(mat1[i][j] + mat2[i][j],end=" ")
    print()

# Pengurangan
for i in range(0,len(mat1)):
    for j in range(0,len(mat1[0])):
        print(mat1[i][j] - mat2[i][j],end=" ")
    print("")

mat1 = [[1,2,3],
        [4,5,6]]
mat2 = [[2,3,4],
        [5,6,7]]
mat3 = []

for x in range(0,len(mat1)):
    row = []
    for y in range(0,len(mat1[0])):
        total = 0
        for z in range(0,len(mat1)):
            total = total + (mat1[x][z] * mat2[z][y])
        row.append(total)
    mat3.append(row)

for i in range(0,len(mat3)):
    for j in range(0,len(mat3[0])):
        print(mat3[i][j],end=" ")
    print("")