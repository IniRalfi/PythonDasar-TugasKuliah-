import operasiAritmatika
print('-----Selamat Datang-----')
while True:
    operasi = int(input('Silahkan pilih operasi yang anda inginkan :\n1. Pertambahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Modulo\n6. Perpangkatan\n7.Keluar\n'))
    if operasi == 1:
        operasiAritmatika.pertambahan()
    elif operasi == 2:
        operasiAritmatika.perkurangan()
    elif operasi == 3:
        operasiAritmatika.perkalian()
    elif operasi == 4:
        operasiAritmatika.pembagian()
    elif operasi == 5:
        operasiAritmatika.modulo()
    elif operasi == 6:
        operasiAritmatika.pangkat()
    elif operasi == 7:
        print('Anda memilih keluar!!! Terima kasih')
        break
    else: 
        print('Silahkan pilih operasi yang benar')