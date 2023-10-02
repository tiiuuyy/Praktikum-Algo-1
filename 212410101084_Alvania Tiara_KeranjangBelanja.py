import os

keranjang = []
harga = []
jumlahtotal = 0
i = 0

while True:
    print('1. Tambah Item \n2. Retur Item \n3. Hentikan Program')
    act = input('Pilih menu nomor : ')
    while act == '1':
        tambah = input('Masukkan barang yang ingin di tambah ke keranjang : ')
        keranjang.append(tambah)
        jumlahtambah = int(input('Masukkan harga barang yang ditambah : '))
        harga.append(jumlahtambah)
        totalharga = sum(harga)

        def clear_screen():
            os.system('cls' if os.name == 'nt' else 'clear')
        clear_screen()
        os.system('cls' if os.name == 'nt' else 'clear')

        print("=" * 55)
        ket = [ 'Nomor', 'Nama', 'Harga']
        print(f'{ket[0]:<10}{ket[1]:<18}{ket[2]:<10}')
        print("=" * 55)

        for x in range(len(keranjang)):
            print(f'{x:<10}{keranjang[x]:<18}{harga[x]:<10}')
        print("=" * 55)
        print(totalharga)
        break
    while act == '2':
        retur = int(input('Pilih barang yang akan dihapus : '))
        jumlahretur = harga[retur]
        keranjang.pop(retur)
        harga.pop(retur)
        totalharga = sum(harga) 

        def clear_screen():
            os.system('cls' if os.name == 'nt' else 'clear')
        clear_screen()
        os.system('cls' if os.name == 'nt' else 'clear')

        print("=" * 55)
        ket = [ 'Daftar', 'Nama', 'Harga Barang']
        print(f'{ket[0]:<10}{ket[1]:<18}{ket[2]:<10}')
        print("=" * 55)

        for x in range(len(keranjang)):
            print(f'{x:<10}{keranjang[x]:<18}{harga[x]:<10}')
        print("=" * 55)
        print(totalharga)
        break
    while act == '3':
        def clear_screen():
            os.system('cls' if os.name == 'nt' else 'clear')
        clear_screen()
        os.system('cls' if os.name == 'nt' else 'clear')

        print("=" * 55)
        ket = [ 'Daftar', 'Nama', 'Harga Barang']
        print(f'{ket[0]:<10}{ket[1]:<18}{ket[2]:<10}')
        print("=" * 55)

        for x in range(len(keranjang)):
            print(f'{x:<10}{keranjang[x]:<18}{harga[x]:<10}')
        print("=" * 55)
        for x in harga:
            jumlahtotal += x
        print('Total yang harus dibayar' , jumlahtotal)
        break