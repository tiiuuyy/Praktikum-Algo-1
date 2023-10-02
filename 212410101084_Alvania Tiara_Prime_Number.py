#program python untuk menentukan bilangan prima atau bukan
print('Prime Number Checker')
nama = 'Alvania Tiara Zulfa'
print('By :' , nama)
nim = 212410101084
print("NIM :" , str(nim))

#meminta input dari user
number = int(input("Masukkan Bilangan : "))
if 2 <= number <= 30:
    if (number==2 or number==3 or number==5 or number==7) or (number%2 != 0 and number%3 != 0 and number%5 != 0 and number%7 != 0):
        print("{} PRIME " .format(number))
    else: 
        print("{} NOT PRIME " .format(number))
else: 
    print("unidentified number")