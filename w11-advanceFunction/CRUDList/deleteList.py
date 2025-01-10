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
            