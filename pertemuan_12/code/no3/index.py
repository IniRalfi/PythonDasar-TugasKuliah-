import CRUD
databaseKaryawan = []

print('Selamat datang di program CRUD Karyawan')
while True :
    print('Silahkan pilih menu operasi yang anda inginkan : ')
    menu = int(input('1. Membuat data karyawan\n2. Menampilkan database karyawan\n3. Mengupdate data karyawan\n4. Menghapus data karyawan\n5. Keluar\nPilihah anda : '))
    if menu == 1:
        data = int(input('Berapa banyak karyawan yang ingin di daftarkan? '))
        for i in range(data):
            isiDb = CRUD.dataKaryawan()
            databaseKaryawan.append(isiDb)
        CRUD.updateDataBase(databaseKaryawan)
    elif menu == 2:
        CRUD.cetakDataKaryawan(databaseKaryawan)
    elif menu == 3:
        print('Untuk mengupdate data karyawan, silahkan masukkan nama karyawan!!!')
        CRUD.editData(databaseKaryawan)
        CRUD.updateDataBase(databaseKaryawan)
    elif menu == 4:
        print('Untuk menghapus data karyawan, silahkan masukkan nama karyawan !!!')
        CRUD.hapusData(databaseKaryawan)
        CRUD.updateDataBase(databaseKaryawan)
    elif menu == 5:
        print('Anda memilih keluar !!! Terima kasih')
        CRUD.updateDataBase(databaseKaryawan)
        break

