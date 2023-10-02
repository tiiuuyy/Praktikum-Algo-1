
game = [
    ['.' , '|' , '.' , '|' , '.'],
    ['.' , '|' , '.' , '|' , '.'],
    ['.' , '|' , '.' , '|' , '.'],
]

kondisi = True
while kondisi :
    pilihxo = 0
    row = 0

    print('\n Main Tic Tac Toe')
    for i in game:
        print(*i,sep='')
    
    print('1. X')
    print('2. O')

    opsi = int(input('Pilih Opsi : '))
    while opsi > 2:
        print('Invalid Input, Try Another One')
        opsi = int(input('Pilih Opsi : '))
    
    urutan = int(input('Mau Isi Di Nomor Berapa? (1-9) :'))
    while urutan > 9:
        print('Invalid Input, Try Another One')
        urutan = int(input('Mau Isi Di Nomor Berapa? (1-9) : '))
    print('=' * 45)
    while True:
        if urutan > 3:
            urutan -= 3
            row += 1
        else :
            if urutan == 1:
                urutan = 0
                break
            elif urutan == 2:
                urutan = 2
                break
            else:
                urutan = 4
                break
    if opsi == 1:
        game[row][urutan] = 'X'
    elif opsi == 2:
        game[row][urutan] = 'O'

    for teliti in game:
        if '.' not in teliti:
            kondisi = False
        else:
            kondisi = True

print('\nTic Tac Toe')
for i in game:
    print(*i,sep='')