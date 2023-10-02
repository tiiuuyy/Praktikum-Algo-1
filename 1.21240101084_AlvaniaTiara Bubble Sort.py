print('Urutan Array List 2D dengan Bubble Sort')
print('=' *39)
number = [
    [20, 1, 13, 50, 35, 62, 73, 66, 54, 2, 12, 22, 36  ],
    [44, 23, 33, 27, 87, 90, 67, 54, 41, 76, 24, 13    ],
    [31, 4, 32, 37, 97, 68, 38, 69, 42, 74, 9, 64, 83  ],
    [21, 46, 67, 55, 47, 17, 53, 29, 39, 70, 35, 15, 28],
]
print('Sebelum diurutkan : ')
for a in number:
    print(a)
print('\n')
for angka_urut in number:
    for x in range(len(angka_urut)):
        for y in range(len(angka_urut)-1):
            if angka_urut[x] < angka_urut[y]:
                angka_urut[x] , angka_urut[y] = angka_urut[y], angka_urut[x]
print('Setelah diurutkan :')
for a in number:
    print(a)