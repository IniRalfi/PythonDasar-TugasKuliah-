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
