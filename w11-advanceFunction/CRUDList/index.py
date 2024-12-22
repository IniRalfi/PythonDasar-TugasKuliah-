import createList
import readList
import updateList
import deleteList
databaseKaryawan = []

print('Selamat datang di program CRUD Karyawan')
while True :
    print('Silahkan pilih menu operasi yang anda inginkan : ')
    menu = int(input('1. Membuat data karyawan\n2. Menampilkan database karyawan\n3. Mengupdate data karyawan\n4. Menghapus data karyawan\n5. Keluar\nPilihah anda : '))
    if menu == 1:
        data = int(input('Berapa banyak karyawan yang ingin di daftarkan? '))
        for i in range(data):
            isiDb = createList.dataKaryawan()
            databaseKaryawan.append(isiDb)
    elif menu == 2:
        readList.cetakDataKaryawan(databaseKaryawan)
    elif menu == 3:
        print('Untuk mengupdate data karyawan, silahkan masukkan nama karyawan!!!')
        updateList.editData(databaseKaryawan)
    elif menu == 4:
        print('Untuk menghapus data karyawan, silahkan masukkan nama karyawan !!!')
        deleteList.hapusData(databaseKaryawan)
    elif menu == 5:
        print('Anda memilih keluar !!! Terima kasih')
        break
