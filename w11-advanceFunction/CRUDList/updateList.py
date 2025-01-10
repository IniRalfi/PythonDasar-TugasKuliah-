
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
                