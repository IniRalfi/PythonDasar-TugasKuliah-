import menu.menu as menu
import format.teksFormat as teksFormat
from datetime import datetime

def catatLog(bill,totalHarga,userName):
    with open('Database/penjualan/historiPenjualan.txt', 'a') as file:
        file.write(f'{datetime.now()}\n')
        file.write(f'Username : {userName}\n')
        for pesanan in bill:
            file.write(f'{pesanan[0]} | {pesanan[1]}\n')
        file.write(f'Total Harga adalah Rp. {teksFormat.format_uang(totalHarga)}\n\n')
        
def tambahUangKas(totalHarga):
    with open('Database/penjualan/uangKas.txt', 'r') as file:
        uangKas = file.read()
    
    uangKasTotal = int(uangKas) + totalHarga
    uangKasTotal = str(uangKasTotal)
    with open('Database/penjualan/uangKas.txt', 'w') as file:
        file.write(uangKasTotal)

def cetakPoin(userName):
    listPoin = []
    with open('Database/databaseAkun/poin_pelanggan.txt', 'r') as file:
        for line in file:
            parts = line.split()
            listPoin.append(parts)
        for user in listPoin:
            if userName == user[0]:
                print(f'Username Anda : {user[0]}\nJumlah Poin Anda : {user[1]}')


def tambahPoin(userName, totalHarga):
    file_akun = 'Database/databaseAkun/akun_user.txt'
    file_poin = 'Database/databaseAkun/poin_pelanggan.txt'

    with open(file_akun, 'r') as file:
        for line in file:
            if userName == line.strip():
                break

    poin_list = []
    with open(file_poin, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                poin_list.append([parts[0], float(parts[1])])

    poin_baru = totalHarga * 0.1
    for data in poin_list:
        if data[0] == userName:  # Jika username ditemukan
            data[1] += poin_baru
            break

    with open(file_poin, 'w') as file:
        for data in poin_list:
            file.write(f"{data[0]} {data[1]:.2f}\n")

    print(f"Poin berhasil ditambahkan. Total poin untuk {userName}: {poin_baru:.2f}")

def pesanMenu(userName):
    while True: 
        operasi = int(input('Anda ingin apa?\n1. Pesan Makanan\n2. Cek Point\n3. Keluar\n'))
        if operasi == 1:
            totalHarga = 0
            bill = []
            print('Silahkan pilih menu yang tersedia')
            menu.tampilkanMenu()
            while True:
                kategori = int(input('Silahkan pilih kategori menu:\n1. Makanan\n2. Minuman\n3. Camilan\n4. Selesai\n>>>Pilihan Anda : '))
                if kategori == 1:
                    with open('Database/dataBaseMenu/menu_makanan.txt', 'r') as file:
                        listMenuMakanan = []
                        for parts in file:
                            makanan = parts.split()
                            namaMakanan = ' '.join(makanan[:-1])
                            harga = makanan[-1]
                            listmenu = [namaMakanan, harga]
                            listMenuMakanan.append(listmenu)
                        print('Silahkan pilih menu makanan')

                    while True:
                        pilihMenu = input('Masukkan nama menu makanan!\nPilihan Anda: ')
                        for makanan in listMenuMakanan:
                            if pilihMenu == makanan[0]:
                                totalHarga += int(makanan[1])
                                pesanan = [makanan[0], makanan[1]]
                                bill.append(pesanan)
                                break
                        else:
                            print('Makanan tidak tersedia di menu')
                        
                        ulang = input('Ingin pesan makanan lagi? y/n: ')
                        if ulang == 'y':
                            continue
                        elif ulang == 'n':
                            print('Terima Kasih')
                            break
                        else:
                            print('Pilihan tidak valid. Keluar.')
                            break

                elif kategori == 2:
                    with open('Database/dataBaseMenu/menu_minuman.txt', 'r') as file:
                        listMenuMinuman = []
                        for parts in file:
                            minuman = parts.split()
                            namaMinuman = ' '.join(minuman[:-1])
                            harga = minuman[-1]
                            listmenu = [namaMinuman, harga]
                            listMenuMinuman.append(listmenu)
                    print('Silahkan pilih menu minuman')

                    while True:
                        pilihMenu = input('Masukkan nama menu minuman!\nPilihan Anda: ')
                        for minuman in listMenuMinuman:
                            if pilihMenu == minuman[0]:
                                totalHarga += int(minuman[1])
                                pesanan = [minuman[0], minuman[1]]
                                bill.append(pesanan)
                                break
                        else:
                            print('Minuman tidak tersedia di menu')

                        ulang = input('Ingin pesan minuman lagi? y/n: ')
                        if ulang == 'y':
                            continue
                        elif ulang == 'n':
                            print('Terima Kasih')
                            break
                        else:
                            print('Pilihan tidak valid. Keluar.')
                            break

                elif kategori == 3:
                    with open('Database/dataBaseMenu/menu_camilan.txt', 'r') as file:
                        listMenuCamilan = []
                        for parts in file:
                            camilan = parts.split()
                            namaCamilan = ' '.join(camilan[:-1])
                            harga = camilan[-1]
                            listmenu = [namaCamilan, harga]
                            listMenuCamilan.append(listmenu)

                    print('Silahkan pilih menu camilan')
                    while True:
                        pilihMenu = input('Masukkan nama menu camilan!\nPilihan Anda: ')
                        for camilan in listMenuCamilan:
                            if pilihMenu == camilan[0]:
                                totalHarga += int(camilan[1])
                                pesanan = [camilan[0], camilan[1]]
                                bill.append(pesanan)
                                break
                        else:
                            print('Camilan tidak tersedia di menu')

                        ulang = input('Ingin pesan camilan lagi? y/n: ')
                        if ulang == 'y':
                            continue
                        elif ulang == 'n':
                            print('Terima Kasih')
                            break
                        else:
                            print('Pilihan tidak valid. Keluar.')
                            break

                elif kategori == 4:
                    print('Pesanan Anda:')
                    for pesanan in bill:
                        print(f'{pesanan[0]} | {pesanan[1]}')
                    print(f'Total Harga adalah Rp. {teksFormat.format_uang(totalHarga)}')
                    tambahPoin(userName,totalHarga)
                    catatLog(bill,totalHarga,userName)
                    tambahUangKas(totalHarga)
                    break
                else:
                    print('Pilihan kategori tidak valid. Silahkan ulangi.')

        elif operasi == 2:
            cetakPoin(userName)

        elif operasi == 3:
            print('Keluar dari sistem. Terima Kasih!')
            break

        else:
            print('Pilihan operasi tidak valid. Silahkan ulangi.')



def loginUser():    
    print('Selamat datang di sistem Informasi Restauran FliFood!!!')
    while True:
        akun = int(input('Silakan anda :\n1. Login (Jika sudah memiliki akun)\n2. Buat Akun(Untuk pengguna Baru)\nPilihan Anda : '))
        if akun == 1:

            akun_user_list = [] 
            with open('Database/databaseAkun/akun_user.txt', 'r') as file:
                for line in file:  # Loop untuk membaca setiap baris dalam file
                    akun_user = line.split()  # Memisahkan setiap baris berdasarkan spasi
                    akun_user_list.append(akun_user)
                
            for attempt in range(3): 
                userName = input('Silahkan Masukkan username akun: ')
                password = input('Silahkan Masukkan password: ')

                for akun_user in akun_user_list:
                    if userName == akun_user[0] and password == akun_user[1]:  # Asumsi format: username password
                        print('Selamat datang!!!')
                        pesanMenu(userName)  
                        return
                print('Username atau password salah')
                if attempt < 2:
                    print(f'Anda memiliki {2 - attempt} kesempatan lagi')
            print("Anda telah mencapai batas percobaan login. Program dihentikan.") 
        
        elif akun == 2:
            print('Selamat datang pengguna baru, silahkan buat akun anda!!!')
            while True:
                userName = input('Silahkan buat user name Anda : ')
                with open('Database/databaseAkun/akun_user.txt', 'r') as file:
                    username_terdaftar = False
                    for line in file:
                        parts = line.split()
                        if parts:
                            if userName == parts[0]:
                                print('Anda tidak dapat menggunakan nomor ini karena nomor Telepon telah di gunakan!')
                                username_terdaftar = True
                                break

                if not username_terdaftar:
                    password = input('Silahkan buat password Anda : ')
                    with open('Database/databaseAkun/akun_user.txt', 'a') as file:
                        file.write(f'{userName} {password}\n')
                    
                    with open('Database/databaseAkun/poin_pelanggan.txt', 'a') as file:   
                        file.write(f'{userName} 0\n')
                    
                    print(f'Akun dengan Username: {userName} dan password {"*" * len(password)} berhasil dibuat!!!')
                    print('Silahkan login menggunakan akun tersebut.')
                    break
                else:
                    continue