# #Program gaji karyawan

gaji_pokok = int(input('Masukkan Gaji Pokok : '))
tunjangan = int (20 / 100 * gaji_pokok)
gaji_kotor = gaji_pokok + tunjangan
pajak = int(15 / 100 * gaji_kotor)
gaji_bersih = gaji_kotor - pajak

print('-----------------------------------------')
print(f'Gaji pokok adalah Rp.{gaji_pokok}')
print(f'Tunjangan Gaji adalah Rp.{tunjangan}')
print(f'Gaji kotor karyawan sebesar Rp.{gaji_kotor}')
print('Potongan pajak sebesar 15% dari gaji kotor')
print(f'Pajak adalah sebesar Rp.{pajak}')
print(f'Gaji Bersih karyawan sebesar Rp.{int(gaji_bersih)}')
print('-----------------------------------------')