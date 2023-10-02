nama = 'Alvania Tiara Zulfa'
nim = 212410101084
print('Nama : ' , nama)
print('NIM : ' , str(nim))

#tugas konversi nilai 
#ppt 04-Percabangan
print('Score Checker')
nilai = int(input('Masukkan Nilai Kamu : '))
if nilai >= 80:
    grade = "A"
elif nilai >= 76:
    grade = "AB"
elif nilai >= 71:
    grade = "B"
elif nilai >= 66:
    grade = "BC"
elif nilai >= 56:
    grade = "C"
elif nilai >= 51:
    grade = "CD"
elif nilai >= 45:
    grade = "D"
elif nilai >= 41:
    grade = "ED"
elif 0 <= nilai <=40:
    grade = "E"
else: 
    grade = "Invalid"

print("Grade : %s " % grade)