# Konversi waktu
total_detik = int(input('Masukkan total detik : '))

if total_detik < 0 :
    print('Anda memasukkan inputan yang salah')
else :
    jam = total_detik // 3600
    sisa_detik = total_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60

    print('-----------------------------------------')
    print(f'Total detik = {total_detik} Detik')
    print(f'Maka konversinya adalah = {jam} Jam {menit} Menit {detik} Detik.')
    print('-----------------------------------------')






# total_detik = int(input('Masukkan total detik : '))
# if total_detik < 0 :
#     print('Anda memasukkan inputan yang salah')
# else :
#     if total_detik < 3600 :
#         if total_detik < 60 :
#                 jam = 0
#                 menit = 0
#                 detik = total_detik
#         else :
#                 jam = 0        
#                 menit = total_detik // 60
#                 detik = total_detik % 60
#     else :
#             jam = total_detik // 3600
#             sisa_detik = total_detik % 3600
#             menit = sisa_detik // 60
#             detik = sisa_detik % 60

#     print('-----------------------------------------')
#     print(f'Total detik = {total_detik} Detik')
#     print(f'Maka konversinya adalah = {jam} Jam {menit} Menit {detik} Detik.')
#     print('-----------------------------------------')
