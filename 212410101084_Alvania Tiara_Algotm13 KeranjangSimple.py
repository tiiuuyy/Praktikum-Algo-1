import os
import csv

gabungan = []
tanggal = []
nama = []
jumlah = []
harga = []
total = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def write_data(variabel):
    with open('penjualan.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Tanggal", "\tNama", "\tJumlah", "\tHarga"])
        writer.writerows(variabel)


while True:
    print('=' * 25)
    print('Pilihan Menu :')
    print('1. Tampilkan Item')
    print('2. Tambah Item')
    print('3. Hapus Item')
    print('4. Hitung harga akhir')
    
    pilihan = int(input('\nMasukkan pilihan nomor \t: '))
    if (pilihan == 1):
        clear_screen()
        print('=' * 57)
        ket = ['No.', 'Tanggal', 'Nama', 'Jumlah', 'Harga']
        print(f'{ket[0]:<8}{ket[1]:<14}{ket[2]:<14}{ket[3]:<14}{ket[4]:<14}')
        print('=' * 57)
        for x in range(len(nama)):
            print(
                f'{x+1:<8}{tanggal[x]:<14}{nama[x]:<14}{jumlah[x]:<14}{harga[x]:<14}')

    elif (pilihan == 2):
        tgl = input('Masukkan tanggal beli \t: ')
        nm = input('Masukkan nama item \t: ')
        jml = int(input('Masukkan jumlah item \t: '))
        hrg = float(input('Masukkan harga item \t: '))
        gabungan.append([tgl, nm, jml, hrg])
        tanggal.append(tgl)
        nama.append(nm)
        jumlah.append(int(jml))
        harga.append(float(hrg))
        print('Data Berhasil Ditambahkan')
        write_data(gabungan)
        clear_screen()

        print('=' * 57)
        ket = ['No.', 'Tanggal', 'Nama', 'Jumlah', 'Harga']
        print(f'{ket[0]:<8}{ket[1]:<14}{ket[2]:<14}{ket[3]:<14}{ket[4]:<14}')
        print('=' * 57)
        for x in range(len(nama)):
            print(
                f'{x+1:<8}{tanggal[x]:<14}{nama[x]:<14}{jumlah[x]:<14}{harga[x]:<14}')

    elif (pilihan == 3):
        index = int(input('Masukkan nomor data yang ingin dihapus : '))
        index -= 1
        tanggal.pop(index)
        nama.pop(index)
        jumlah.pop(index)
        harga.pop(index)
        gabungan.pop(index)
        write_data(gabungan)
        print('Data berhasil dihapus')
        clear_screen()
        print('=' * 57)
        ket = ['No.', 'Tanggal', 'Nama', 'Jumlah', 'Harga']
        print(f'{ket[0]:<8}{ket[1]:<14}{ket[2]:<14}{ket[3]:<14}{ket[4]:<14}')
        print('=' * 57)
        for x in range(len(nama)):
            print(
                f'{x+1:<8}{tanggal[x]:<14}{nama[x]:<14}{jumlah[x]:<14}{harga[x]:<14}')

    elif (pilihan == 4):
        clear_screen()
        print('=' * 57)
        ket = ['No.', 'Tanggal', 'Nama', 'Jumlah', 'Harga']
        print(f'{ket[0]:<8}{ket[1]:<14}{ket[2]:<14}{ket[3]:<14}{ket[4]:<14}')
        print('=' * 57)
        for x in range(len(nama)):
            print(
                f'{x+1:<8}{tanggal[x]:<14}{nama[x]:<14}{jumlah[x]:<14}{harga[x]:<14}')
        for x in harga:
            total = sum(harga)
        print('=' * 57)
        print('Total Harga \t: ', total)
    else:
        print('Pilihan tidak valid. Menutup program...')