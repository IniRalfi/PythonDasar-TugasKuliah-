import admin
import user
import format.teksFormat as teksFormat

def pilihRole():
    teksFormat.dekorasi(100)
    print("Selamat Datang di ")
    print("Sistem Informasi Restoran Flifood")
    print("Nikmati pengalaman kuliner terbaik bersama kami!")
    teksFormat.dekorasi(100)
    
    while True:
        userRole = int(input('Anda akan login sebagai?\n1. Admin\n2. User\n3. Batal\nPilihan Anda : '))
        if userRole == 1:
            admin.loginAdmin()
        elif userRole == 2:
            user.loginUser()
        elif userRole == 3:
            print('Operasi di batalkan oleh pengguna')
            break
        else:
            print('Silahkan masukkan pilihan yang benar')
pilihRole()