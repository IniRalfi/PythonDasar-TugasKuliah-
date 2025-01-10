import format.teksFormat as teksFormat
from menu import menu

def cekUangKas ():
    with open('Database/penjualan/uangKas.txt', 'r') as uang:
        uangKas = int(uang.read())
    print(f'Total uang kas restaurant adalah Rp.{teksFormat.format_uang(uangKas)}')
    return uangKas

def cetakDatabasePelanggan():
    listAkunUser = []
    listPoinUser = []
    listGabungan = []
    with open('Database/databaseAkun/akun_user.txt', 'r') as file:
        for lines in file:
            akun = lines.split()
            listAkunUser.append(akun)
    
    with open('Database/databaseAkun/poin_pelanggan.txt', 'r') as file:
        for lines in file:
            poin = lines.split()
            listPoinUser.append(poin[-1])
    
    for i in range(len(listAkunUser)):
        akun = listAkunUser[i]
        poin = listPoinUser[i]
        akunPoin = akun + [poin]
        listGabungan.append(akunPoin)
    
    print('Berikut adalah daftar Akun User : ')
    teksFormat.dekorasiGaris(50)
    for listAkun in listGabungan:
        print(f'UserName : {listAkun[0]}\nPassword : {listAkun[1]}\nTotal Poin : {listAkun[2]}\n')

def loginAdmin():
    print('Anda memilih menu admin, pastikan ini benar Anda!!!')
    admin = 'admin'
    password = 'admin#123'

    for attempt in range(3):
        adminName = input('Silahkan masukkan username admin Anda (admin): ')
        passwordAdmin = input('Silahkan masukkan password (admin#123): ')

        if adminName == admin and passwordAdmin == password:
            print()
            teksFormat.dekorasi(100)
            print('Selamat datang di menu Admin')
            while True:
                menuAdmin = int(input('Silahkan pilih menu yang ingin Anda gunakan:\n1. Cek uang Kas Restaurant\n2. Kelola Menu Restaurant\n3. Cek Database Pelanggan\n4. Keluar\nPilihan Anda : '))
                if menuAdmin == 1:
                    teksFormat.dekorasi(50)
                    cekUangKas()
                    
                elif menuAdmin == 2:
                    teksFormat.dekorasi(50)
                    print('Selamat datang di sistem pengelolaan menu!')
                    while True:
                        teksFormat.dekorasiGaris(50)
                        operasiMenu = int(input('Silahkan pilih menu berikut :\n1. Tambah Menu\n2. Hapus Menu\n3. Edit Harga Menu\n4. Tampilkan Menu\n5. Keluar\nPilihan Anda : '))
                        if operasiMenu == 1:
                            menu.tambahMenu()
                        elif operasiMenu == 2:
                            menu.hapusMenu()
                        elif operasiMenu == 3:
                            menu.updateMenu()
                        elif operasiMenu == 4:
                            menu.tampilkanMenu()
                        elif operasiMenu == 5:
                            break
                elif menuAdmin == 3:
                    cetakDatabasePelanggan()
                elif menuAdmin == 4:
                    print('Anda memilih keluar, terima kasih')
                    break
                else:
                    print('Silahkan masukkan pilihan yang benar!!!')
                return
        
        else:
            print('Username atau password tidak valid.')
            if attempt < 2:
                print(f'Anda memiliki {2 - attempt} percobaan lagi.')
    
    print('Anda telah gagal login sebanyak 3 kali. Kembali ke menu utama.')
