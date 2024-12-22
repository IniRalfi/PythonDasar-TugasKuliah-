def dataKaryawan():
    listKaryawan = []
    def daftarKaryawan():
        namaKaryawan = input('Masukkan Nama Karyawan : ').upper()
        umur = int(input('Masukkan Umur Karyawan : '))
        gaji = int(input('Masukkan gaji pokok karyawan : '))
        return namaKaryawan, umur, gaji

    def simpanDataKaryawan(namaKaryawan, umur, gaji):
        listKaryawan.append(namaKaryawan)
        listKaryawan.append(umur)
        listKaryawan.append(gaji)
        print('Data Karyawan berhasil di simpan')
        print('------------------------------------------------')

    namaKaryawan, umur, gaji= daftarKaryawan()
    simpanDataKaryawan(namaKaryawan, umur, gaji)
    return listKaryawan
    
    
def cetakDataKaryawan(databaseKaryawan):
    jmldata = 3
    print()
    print('Berikut adalah data Karyawan: ')
    print('-------------------------------------------------------------------------')
    print(f'|\tNama Karyawan\t|\tUmur Karyawan\t|\tGaji Karyawan\t|')
    print('-------------------------------------------------------------------------')
    for i in range (len(databaseKaryawan)):
        print(f'|\t  {databaseKaryawan[i][jmldata-jmldata]}  \t|\t  {databaseKaryawan[i][jmldata-2]}  \t\t|\t  {databaseKaryawan[i][jmldata-1]}  \t|')
        print('-------------------------------------------------------------------------')
        print()



def editData(databaseKaryawan):
    if len(databaseKaryawan) == 0:
        print('Data masih kosong!!!')
        print()
    else:
        namaKaryawan = input('Masukkan nama karyawan yang ingin di edit : ').upper()
        for karyawan in databaseKaryawan:
                if namaKaryawan == karyawan[0]:
                    print(f'Data ditemukan {karyawan} silahkan edit data tersebut')
                    karyawan.clear()
                    namaKaryawanBaru = input('Masukkan Nama karyawan yang baru : ').upper()
                    umur = int(input('Masukkan umur karyawan : '))
                    gaji = int(input('Masukkan gaji pokok karyawan : '))
                    karyawan.append(namaKaryawanBaru)
                    karyawan.append(umur)
                    karyawan.append(gaji)
                    print('Data berhasil di edit')
                    print('-------------------------------------------')
                    print()
                else:
                    print('Data karyawan tidak ditemukan.')
                    print()

def hapusData(databaseKaryawan):
    namaKaryawan = input('Masukkan nama karyawan yang ingin dihapus: ').upper()
    dataDitemukan = False
    
    for i in range(len(databaseKaryawan)):
        if namaKaryawan == databaseKaryawan[i][0].upper():
            dataDitemukan = True
            print(f'Data ditemukan: {databaseKaryawan[i]}, silakan hapus data tersebut.')
            permission = input('Apakah Anda ingin menghapus data ini? y/n: ').lower()
            
            if permission == 'y':
                del databaseKaryawan[i]
                print('Data berhasil dihapus.')
                print()
            else:
                print('Data tidak dihapus.')
                print()
            break
    
    if dataDitemukan == False:
        print('Data karyawan tidak ditemukan.')
        print()

def updateDataBase(databaseKaryawan):
    with open('dataBase.txt', 'w') as database:
        pass
    for data in databaseKaryawan:
        nama = data[0]
        umur = data[1]
        gaji = data[2]
        with open('dataBase.txt', 'a') as database:
            database.write(f'\nNama Karyawan : {nama}')
            database.write(f'\nUmur Karyawan : {umur}')
            database.write(f'\nGaji Pokok Karyawan : {gaji}')
            database.write('\n')
            