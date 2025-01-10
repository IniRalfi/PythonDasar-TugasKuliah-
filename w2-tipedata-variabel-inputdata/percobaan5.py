# konversi Jam menit detik ke total detik
total_jam = int(input('Masukkan Total jam : '))
while total_jam < 0 :
    print('---------------Warning----------------')
    print('Masukkan kembali total jam')
    total_jam = int(input('Masukkan Total jam : '))

total_menit = int(input('Masukkan Total menit : '))
while total_menit < 0 :
    print('---------------Warning----------------')
    print('Masukkan kembali total menit')
    total_menit = int(input('Masukkan Total menit : '))

detik = int(input('Masukkan Total detik : '))

print('-----------------------------------------')
jam = total_jam * 3600
menit = total_menit * 60
total_detik = jam + menit + detik
print(f'Waktu nya adalah {total_jam} Jam {total_menit} Menit {detik} Detik')
print(f'Total detik adalah : {total_detik} Detik')
print('-----------------------------------------') 