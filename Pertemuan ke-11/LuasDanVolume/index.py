import bangunDatar
import bangunRuang
while True:
    operasi = int(input('Silahkan pilih Operasi : \n1. Mengitung Luas Bangun datar \n2. Menghitung Volume Bangun ruang\n3. Keluar\nPilihan anda : '))
    if operasi == 1:
        print('Anda memilih opsi 1. menghitung luas bangun datar, Silahkan pilih bangun datar yang anda inginkan')
        bangunDatar.luasBangunDatar()    
    elif operasi == 2:
        print('Anda memilih opsi 2. menghitung luas bangun ruang, Silahkan pilih bangun ruang yang anda inginkan')
        bangunRuang.volumeBangunRuang()
    elif operasi == 3:
        print('Anda memilih keluar, Terima kasih')
        break
    else:
        print('Silahkan masukkan pilihan operasi yang tepat')
