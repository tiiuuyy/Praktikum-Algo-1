#Membuat Program manipulasi NIM, kemudian memunculkan kode prodi dan angkatan
#pakai operasi aritmatika
#Nama : Alvania Tiara Zulfa
#Kelas : B

print('\nKode Prodi dan Angkatan Checker')
dataNIM = int(input('Masukkan NIM : '))
print('===========================')

prodi = ((dataNIM // 1000) % 10)
print('Kode Prodi : {}' .format(prodi))
ang = (dataNIM // 10**10)
print('Kode Angkatan : {}' .format(ang))