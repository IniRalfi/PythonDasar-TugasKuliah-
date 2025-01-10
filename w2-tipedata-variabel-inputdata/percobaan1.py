# Mengitung harga barang + ppn

nama_barang = input('Input nama barang : ')
harga_barang = int(input('Input masukkan harga barang : '))
pajak = 12.5 / 100 * harga_barang 
total_harga = pajak + harga_barang
print(f'Nama barang : {nama_barang}')
print(f'Harga barang : Rp.{harga_barang}')
print(f'Pajak yang harus di bayar adalah : Rp.{int(pajak)}')
print(f'Total harga yang harus di bayar adalah Rp.{int(total_harga)}')