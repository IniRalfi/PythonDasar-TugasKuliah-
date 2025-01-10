
from format import teksFormat


listMenu = []
            
# Creatae
def tambahMenu():
    print('Silahkan tambahkan nama menu dan harga')
    while True:
        teksFormat.dekorasi(100)
        pilih = int(input('Jenis menu apa yang ingin anda tambah :\n1. Makanan\n2. Minuman\n3. Desert dan Cemilan\n4. Simpan perubahan\nPilihan anda : '))
        if pilih == 4:
            print('Perubahan berhasil di simpan!')
            break
        namaMenu = input('Masukkan nama menu : ')
        harga = input('Masukkan harga menu : ')
        if pilih == 1:
            with open('Database/databaseMenu/menu_makanan.txt', 'a') as menu:
                menu.write(f'{namaMenu} ')
                menu.write(f'{harga}\n')
            print('menu berhasil di tambahkan!')  
        elif pilih == 2:     
            with open('Database/databaseMenu/menu_minuman.txt', 'a') as menu:
                menu.write(f'{namaMenu} ')
                menu.write(f'{harga}\n')
            print('menu berhasil di tambahkan!')     
        elif pilih == 3:
            with open('Database/databaseMenu/menu_camilan.txt', 'a') as menu:
                menu.write(f'{namaMenu} ')
                menu.write(f'{harga}\n')    
        else : 
            print('Silahkan Masukkan Pilihan yang benar')
            
# Read
def tampilkanMenu():  
    listMenuMakanan = []
    with open("Database/databaseMenu/menu_makanan.txt", "r") as file:
        for line in file:
            parts = line.split()

            if len(parts) > 1:
                nama_barang = " ".join(parts[:-1])
                harga = parts[-1]
            else:
                nama_barang = parts[0]
                harga = "Tidak ada harga"

            result = [nama_barang, harga]
            listMenuMakanan.append(result)   
            
    listMenuMinuman = []
    with open("Database/databaseMenu/menu_minuman.txt", "r") as file:
        for line in file:
            parts = line.split()

            if len(parts) > 1:
                nama_barang = " ".join(parts[:-1])
                harga = parts[-1]
            else:
                nama_barang = parts[0]
                harga = "Tidak ada harga"

            result = [nama_barang, harga]
            listMenuMinuman.append(result)
    
    listMenuCamilan = []
    with open("Database/databaseMenu/menu_camilan.txt", "r") as file:
        for line in file:
            parts = line.split()

            if len(parts) > 1:
                nama_barang = " ".join(parts[:-1])
                harga = parts[-1]
            else:
                nama_barang = parts[0]
                harga = "Tidak ada harga"

            result = [nama_barang, harga]
            listMenuCamilan.append(result)
            
    teksFormat.dekorasi(100)
    print(f'|\t\t\tMenu\t\t\t |\t\t\tHarga\t\t\t   |')
    teksFormat.dekorasiGaris(100)
    print(f'|\t\t\t\t\t\tMakanan')
    teksFormat.dekorasiGaris(100)
    for menu in listMenuMakanan:
        print(f'|\t\t{menu[0]}\t\t\t |\t\t\t{menu[1]}\t\t\t   |')
    teksFormat.dekorasiGaris(100)
    print(f'|\t\t\t\t\t\tMinuman')
    teksFormat.dekorasiGaris(100)
    for menu in listMenuMinuman:
        print(f'|\t\t{menu[0]}\t\t\t |\t\t\t{menu[1]}\t\t\t   |')
    teksFormat.dekorasiGaris(100)
    print(f'|\t\t\t\t\t\tCamilan')
    teksFormat.dekorasiGaris(100)    
    for menu in listMenuCamilan:
        print(f'|\t\t{menu[0]}\t\t\t |\t\t\t{menu[1]}\t\t\t   |')
    teksFormat.dekorasi(100) 
    return listMenuMakanan



def updateMenu():
    print('Silahkan pilih menu yang ingin di update.')
    listMenuMakanan = []
    with open("Database/databaseMenu/menu_makanan.txt", "r") as file:
        for line in file:
            parts = line.split()

            if len(parts) > 1:
                nama_barang = " ".join(parts[:-1])
                harga = parts[-1]
            else:
                nama_barang = parts[0]
                harga = "Tidak ada harga"

            result = [nama_barang, harga]
            listMenuMakanan.append(result)
    
    listMenuMinuman = []
    with open("Database/databaseMenu/menu_minuman.txt", "r") as file:
        for line in file:
            parts = line.split()

            if len(parts) > 1:
                nama_barang = " ".join(parts[:-1])
                harga = parts[-1]
            else:
                nama_barang = parts[0]
                harga = "Tidak ada harga"

            result = [nama_barang, harga]
            listMenuMinuman.append(result)
    
    listMenuCamilan = []
    with open("Database/databaseMenu/menu_camilan.txt", "r") as file:
        for line in file:
            parts = line.split()

            if len(parts) > 1:
                nama_barang = " ".join(parts[:-1])
                harga = parts[-1]
            else:
                nama_barang = parts[0]
                harga = "Tidak ada harga"

            result = [nama_barang, harga]
            listMenuCamilan.append(result)
            
    while True:
        teksFormat.dekorasi(100)
        pilih = int(input('Kategori menu yang akan di edit :\n1. Makanan\n2. Minuman\n3. Camilan\n4. Simpan dan Keluar\n'))
        if pilih == 1:
            print('Daftar Menu : ')
            for menu in listMenuMakanan:
                print(f'{menu[0]}')

            menuEdit = input('Silahkan masukkan menu yang ingin anda edit : ')
            menuDitemukan = False
            for menu in listMenuMakanan:
                if menuEdit == menu[0]:
                    menuLama = menu
                    menu[0] = input('Silahkan masukkan nama menu yang baru : ')
                    menu[1] = input('Silahkan masukkan harga menu : ')
                    print(f'menu {menuLama} telah di edit menjadi [{menu[0]},{menu[1]}]')
                    menuDitemukan = True  # Mengubah status menjadi True jika ditemukan
                    break

            if not menuDitemukan:
                print('Menu tidak ditemukan.')
                return

            with open('Database/databaseMenu/menu_makanan.txt', 'w') as file:
                for menu in listMenuMakanan:
                    file.write(f'{menu[0]} {menu[1]}\n')

        elif pilih == 2:
            print('Daftar Menu : ')
            for menu in listMenuMinuman:
                print(f'{menu[0]}')

            menuEdit = input('Silahkan masukkan menu yang ingin anda edit : ')
            menuDitemukan = False
            for menu in listMenuMinuman:
                if menuEdit == menu[0]:
                    menuLama = menu
                    menu[0] = input('Silahkan masukkan nama menu yang baru : ')
                    menu[1] = input('Silahkan masukkan harga menu : ')
                    print(f'menu {menuLama} telah di edit menjadi [{menu[0]},{menu[1]}]')
                    menuDitemukan = True  # Mengubah status menjadi True jika ditemukan
                    break

            if not menuDitemukan:
                print('Menu tidak ditemukan.')
                return

            with open('Database/databaseMenu/menu_minuman.txt', 'w') as file:
                for menu in listMenuMinuman:
                    file.write(f'{menu[0]} {menu[1]}\n')

        elif pilih == 3:
            print('Daftar Menu : ')
            for menu in listMenuCamilan:
                print(f'{menu[0]}')

            menuEdit = input('Silahkan masukkan menu yang ingin anda edit : ')
            menuDitemukan = False
            for menu in listMenuCamilan:
                if menuEdit == menu[0]:
                    menuLama = menu
                    menu[0] = input('Silahkan masukkan nama menu yang baru : ')
                    menu[1] = input('Silahkan masukkan harga menu : ')
                    print(f'menu {menuLama} telah di edit menjadi [{menu[0]},{menu[1]}]')
                    menuDitemukan = True  # Mengubah status menjadi True jika ditemukan
                    break

            if not menuDitemukan:
                print('Menu tidak ditemukan.')
                return

            with open('Database/databaseMenu/menu_camilan.txt', 'w') as file:
                for menu in listMenuCamilan:
                    file.write(f'{menu[0]} {menu[1]}\n')

        elif pilih == 4:
            print('Semua perubahan berhasil disimpan.')
            break
        else:
            print('Silahkan Masukkan pilihan yang benar')

# Delete
def hapusMenu():
    print('Silahkan pilih menu yang akan di hapus')
    listMenuMakanan = []
    with open("Database/databaseMenu/menu_makanan.txt", "r") as file:
        for line in file:
            parts = line.split()

            if len(parts) > 1:
                nama_barang = " ".join(parts[:-1])
                harga = parts[-1]
            else:
                nama_barang = parts[0]
                harga = "Tidak ada harga"

            result = [nama_barang, harga]
            listMenuMakanan.append(result)
    
    listMenuMinuman = []
    with open("Database/databaseMenu/menu_minuman.txt", "r") as file:
        for line in file:
            parts = line.split()

            if len(parts) > 1:
                nama_barang = " ".join(parts[:-1])
                harga = parts[-1]
            else:
                nama_barang = parts[0]
                harga = "Tidak ada harga"

            result = [nama_barang, harga]
            listMenuMinuman.append(result)
    
    listMenuCamilan = []
    with open("Database/databaseMenu/menu_camilan.txt", "r") as file:
        for line in file:
            parts = line.split()

            if len(parts) > 1:
                nama_barang = " ".join(parts[:-1])
                harga = parts[-1]
            else:
                nama_barang = parts[0]
                harga = "Tidak ada harga"

            result = [nama_barang, harga]
            listMenuCamilan.append(result)

    while True: 
        pilih = int(input('Kategori Makanan yang ingin anda hapus : \n1. Makanan\n2. Minuman\n3. Camilan\n4. Simpan dan Keluar'))  
        if pilih == 1:  
            print('Daftar Menu : ')
            
            for menu in listMenuMakanan:
                print(f'{menu[0]}')
            
            menuHapus = input('Silahkan masukkan menu yang ingin di hapus : ')    
            menuDitemukan = False
            for menu in listMenuMakanan:
                if menuHapus == menu[0]:
                    listMenuMakanan.remove(menu)
                    menuDitemukan = True  
                    print(f'{menu} Telah di hapus dari daftar menu.')
                    break
            
            if not menuDitemukan:  
                print(f'Menu {menuHapus} Tidak di temukan.')
                return
            
            with open('Database/databaseMenu/menu_makanan.txt', 'w') as file:
                for menu in listMenuMakanan:
                    file.write(f'{menu[0]} {menu[1]}\n')
            
        elif pilih == 2:
            print('Daftar Menu : ')
            
            for menu in listMenuMinuman:
                print(f'{menu[0]}')
            
            menuHapus = input('Silahkan masukkan menu yang ingin di hapus : ')    
            menuDitemukan = False
            for menu in listMenuMinuman:
                if menuHapus == menu[0]:
                    listMenuMinuman.remove(menu)
                    menuDitemukan = True  
                    print(f'{menu} Telah di hapus dari daftar menu.')
                    break
            
            if not menuDitemukan:  
                print(f'Menu {menuHapus} Tidak di temukan.')
                return
            
            with open('Database/databaseMenu/menu_minuman.txt', 'w') as file:
                for menu in listMenuMinuman:
                    file.write(f'{menu[0]} {menu[1]}\n')
        
        elif pilih == 3:
            print('Daftar Menu : ')
            
            for menu in listMenuCamilan:
                print(f'{menu[0]}')
            
            menuHapus = input('Silahkan masukkan menu yang ingin di hapus : ')    
            menuDitemukan = False
            for menu in listMenuCamilan:
                if menuHapus == menu[0]:
                    listMenuCamilan.remove(menu)
                    menuDitemukan = True  
                    print(f'{menu} Telah di hapus dari daftar menu.')
                    break
            
            if not menuDitemukan:  
                print(f'Menu {menuHapus} Tidak di temukan.')
                return
            
            with open('Database/databaseMenu/menu_camilan.txt', 'w') as file:
                for menu in listMenuCamilan:
                    file.write(f'{menu[0]} {menu[1]}\n')
        elif pilih == 4:
            print('Anda memilih keluar Terima kasih!')
            break