print('-----------------------------------------')

jam_mulai = int(input('Masukkan jam mulai : '))
menit_mulai = int(input('Masukkan menit mulai : '))
detik_mulai = int(input('Masukkan detik mulai : '))
total_detik_jam_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
print('-----------------------------------------')


jam_selesai = int(input('Masukkan jam keluar : '))
while jam_selesai < jam_mulai: 
    print('---------------Warning----------------')
    print('Jam yang anda masukkan salah, silahkan inputkan kembali')
    jam_selesai = int(input('Masukkan jam keluar : '))

menit_selesai = int(input('Masukkan menit keluar : '))
detik_selesai = int(input('Masukkan detik keluar : '))
total_detik_jam_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai


lama_pemakaian = total_detik_jam_selesai - total_detik_jam_mulai


lama_jam = round(lama_pemakaian / 3600, 1)
jam_pakai = lama_pemakaian / 3600
jam_pakai = int(jam_pakai) if jam_pakai == int(jam_pakai) else int(jam_pakai) + 1  # Membulatkan ke atas

if jam_pakai <= 1:
    biaya = 5000
else:
    biaya =(jam_pakai - 1) * 10000

print('-----------------------------------------')
print(f'Jam mulai adalah pada Pukul {jam_mulai}:{menit_mulai}:{detik_mulai}')
print(f'Jam selesai adalah pada Pukul {jam_selesai}:{menit_selesai}:{detik_selesai}')
print(f'Lama pemakaian adalah {lama_jam} Jam')
print(f'Total tarif yang harus di bayar adalah Rp.{biaya}')
print('-----------------------------------------')
