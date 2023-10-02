mtrx1 = [
    [1, 2],
    [3, 4],
]

mtrx2 = [
    [2, 1],
    [1, 4],
]

hasil =[]

for x in range(0, len(mtrx1)):
    row = []
    for y in range(0, len(mtrx2[0])):
        total = 0
        for z in range(0, len(mtrx1)):
            total = total + (mtrx1[x][z] * mtrx2[z][y])
        row.append(total)
    hasil.append(row)

for row in hasil:
    print(row)
