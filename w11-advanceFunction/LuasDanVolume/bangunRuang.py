def volumeBangunRuang():
    bangunRuang = int(input('Silahkan pilih bangun datar:\n1. Kubus\n2. Balok\n3. Limas Segi Empat\n4. Prisma Segi Tiga\n5. Limas Segi Tiga\n6. Silinder\n7. Kerucut\n8. Bola\n9. Pilihan Anda : '))
    def kubus():
        a = int(input('Masukkan sisi a: '))
        volumeKubus = a * a * a
        print(f'Volume kubus dengan sisi {a}cm adalah {volumeKubus} cm3')
        return volumeKubus
    
    def balok():
        p = int(input('Masukkan panjang: '))
        l = int(input('Masukkan lebar: '))
        t = int(input('Masukkan tinggi : '))
        volumeBalok = p*l*t
        print(f'Volume balok dengan panjang{p} cm lebar {l}cm dan tinggi {t}cm adalah {volumeBalok}cm3')
        return volumeBalok
    
    def limasSegiEmpat():
        p = int(input('Masukkan sisi alas : '))
        l = int(input('Masukkan sisi alas : '))
        t = int(input('Masukkan tinggi limas : '))
        la = p * l
        volumeLimasSegiEmpat = 1/3 * la * t
        print(f'Volume limas segi empat dengan luas alas {la} cm2 dan tinggi {t} cm adalah {volumeLimasSegiEmpat}cm3')
        return volumeLimasSegiEmpat
    
    def prismaSegiTiga():
        a = int(input('Masukkan alas  : '))
        t = int(input('Masukkan tinggi alas : '))
        T = int(input('Masukkan tinggi prisma : '))
        la = 1/2 * a * T
        volumePrismaSegiTiga = la * T
        print(f'Volume prisma segitiga dengan luas alas {la}cm2 dan tinggi {T}cm adalah {volumePrismaSegiTiga}cm3')
        return volumePrismaSegiTiga
    
    def limasSegiTiga():
        a = int(input('Masukkan alas segitiga : '))
        t = int(input('Masukkan tinggi segitiga : '))
        T = int(input('Masukkan tinggi prisma : '))
        la = 1/2 * a * T
        volumeLimasSegiTiga = 1/3 * la * T
        print(f'Volume limas segitiga dengan luas alas {la}cm2 dan tinggi {T}cm adalah {volumeLimasSegiTiga}cm3')
        return volumeLimasSegiTiga
    
    def silinder():
        phi = 3.14
        r = int(input('Masukkan jari jari alas : '))
        t = int(input('Masukkan tinggi silinder : '))
        volumeSilinder = phi *r*r * t
        print(f'Volume silinder dengan jari jari {r} cm dan tinggi {t} cm adalah {volumeSilinder}cm3')
        return volumeSilinder
    
    def kerucut():
        phi = 3.14
        r = int(input('Masukkan jari jari alas : '))
        t = int(input('Masukkan tinggi silinder : '))
        volumeKerucut = 1/3 * phi * pow(r,r) * t
        print(f'Volume kerucut dengan jari jari {r} cm dan tinggi {t} cm adalah {volumeKerucut}cm3')
        return volumeKerucut
    
    def bola():
        phi = 3.14
        r = int(input('Masukkan jari jari alas : '))
        volumeBola = 4/3 * phi * r*r*r
        print(f'Volume bola dengan jari jari {r} cm adalah {volumeBola}cm3')
        return volumeBola
    
    if bangunRuang == 1:
        kubus()
        print()
    elif bangunRuang == 2:
        balok()
        print()
    elif bangunRuang == 3:
        limasSegiEmpat()
        print()
    elif bangunRuang == 4:
        prismaSegiTiga()
        print()
    elif bangunRuang == 5:
        limasSegiTiga()
        print()
    elif bangunRuang == 6:
        silinder()
        print()
    elif bangunRuang == 7:
        kerucut()
        print()
    elif bangunRuang == 8:
        bola()
        print()
    else:
        print('Silahkan masukkan pilihan yang benar')