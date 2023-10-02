#INPUT EDIT LIST ITEM DARI USER
print('List Item')
item = ['foam','toner','cleanser','serum','niacinamide', 'cream', 'gel', 'moisturizer', 'sunscreen', 'mask']
print(item , '\n')
print('=' * 55)
print('ketik "tambah" kalau mau tambah item baru')
print('ketik "buang" kalau ingin membuang salah satu item')
print('ketik "done" ketika tidak ada yang diubah lagi')
print('=' * 55)

while True:
    command = input('Ubah item dengan [tambah/buang/done] :')
    if command == 'tambah':
        tambah = input('Masukkan item yang akan ditambahkan:')
        item.append(tambah)
        print(tambah, 'Data telah ditambahkan')
    
    if command == 'buang':
        buang = input('Masukkan item yang ingin dibuang :')
        item.remove(buang)
        print(buang, 'item telah dibuang dari list')
    
    if command == 'done':
        break

print('=' * 55)
#MENGURUTKAN DATA ITEM SESUAI ABJAD
print('\nUrutan Item Sesuai Abjad')
for i in range(len(item)-1):
    for x in range(len(item)-i-1):
        if (item[x+1] < item[x] ):
            item[x], item[x+1] = item[x+1], item[x]
print(item)            
print('=' * 55)
#MENGURUTKAN DATA ITEM SESUAI PANJANG KATA
print('Urutan Sesuai Panjang Huruf dalam Kata')
for i in range(len(item) -1):
    for x in range(len(item)-1):
        if len(item[x]) > len(item[x+1]) :
            item[x], item[x+1] = item[x] , item[x+1]

print('\nData Item Anda sudah urut sesuai panjang kata :')
list_item = len(item)
for i in range(list_item):
    for x in range(list_item):
        if len(item[i]) < len(item[x]):
            d = item[i]
            item[i] = item [x]
            item[x] = d
print(item)