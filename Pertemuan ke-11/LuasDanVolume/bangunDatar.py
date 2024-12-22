def luasBangunDatar():
            
    def persegi():
        a = int(input('Masukkan sisi persegi: '))
        luasPersegi = a * a
        print(f'Luas persegi dengan sisi {a} cm dan {a} cm adalah {luasPersegi} cm2')
        return luasPersegi

    def persegiPanjang():
        a = int(input('Masukkan panjang: '))
        b = int(input('Masukkan lebar: '))
        luasPersegiPanjang = a * b
        print(f'Luas persegi panjang dengan panjang {a} cm dan lebar {b} cm adalah {luasPersegiPanjang} cm2')
        return luasPersegiPanjang    

    def segitiga():
        a = int(input('Masukkan sisi alas: '))
        t = int(input('Masukkan tinggi: '))
        luasSegitiga = (a * t) / 2
        print(f'Luas segitiga dengan alas {a} cm dan tinggi {t} cm adalah {luasSegitiga} cm2')
        return luasSegitiga  

    def jajarGenjang():
        a = int(input('Masukkan alas : '))
        t = int(input('Masukkan tinggi : '))
        luasJajarGenjang = a * t
        print(f'Luas jajar genjang dengan alas {a} cm dan tinggi {t} cm adalah {luasJajarGenjang} cm2')
        return luasJajarGenjang
    
    def belahKetupat():
        d1 = int('Masukkan Diagonal 1 : ')
        d2 = int('Masukkan Diagonal 2 : ')
        luasBelahKetupat = 0.5 * d1 * d2
        print(f'Luas belah ketupat dengan diagonal 1 {d1} cm dan diagonal 2 {d2} cm adalah {luasBelahKetupat} cm2')
        return luasBelahKetupat
    
    def layangLayang ():
        d1 = int('Masukkan Diagonal 1 : ')
        d2 = int('Masukkan Diagonal 2 : ')
        luasLayangLayang = 0.5 * d1 * d2
        print(f'Luas layang-layang dengan diagonal 1 {d1} cm dan diagonal 2 {d2} cm adalah {luasLayangLayang} cm2')
        return luasLayangLayang
    
    def trapesium():
        a = int(input('Masukkan panjang: '))
        b = int(input('Masukkan lebar: '))
        t = int(input('Masukkan tinggi : '))
        luasTrapesium = (a + b)/2 * t
        print(f'Luas Trapesium dengan sisi {a} cm dan {b} cm dengan tinggi {t}cm adalah {trapesium} cm2')
        return luasTrapesium
    
    def lingkaran():
        phi = 3.14
        r = int(input('Masukkan jari jari lingkaran : '))
        luasLingkaran = phi * pow(r,r)
        print(f'Luas Lingkaran dengan jari-jari {r} cm adalah {luasLingkaran} cm2')
        return luasLingkaran
        
            
    bangunDatar = int(input('Silahkan pilih bangun datar:\n1. Persegi\n2. Persegi panjang\n3. Segitiga\n4. Jajar Genjang\n5. Belah Ketupat\n6. Layang - Layang\n7. Trapesium\n8. Lingkaran\npilihan anda : '))
    if bangunDatar == 1:
        persegi()
        print()
    elif bangunDatar == 2:
        persegiPanjang()
        print()
    elif bangunDatar == 3:
        segitiga()
        print()
    elif bangunDatar == 4:
        jajarGenjang()
        print()
    elif bangunDatar == 5:
        belahKetupat()
        print()
    elif bangunDatar == 6:
        layangLayang()
        print()
    elif bangunDatar == 7:
        trapesium()
        print()
    elif bangunDatar == 8:
        lingkaran()
        print()
    else:
        print('Silahkan masukkan pilihan yang benar')

        