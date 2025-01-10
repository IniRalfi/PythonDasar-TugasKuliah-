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
    