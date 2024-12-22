def pertambahan ():
    print('Anda memilih operasi pertambahan')
    a = int(input('Masukkan angka pertama : '))
    b = int(input('Masukkan angka kedua : '))
    print(f'Hasil pertambahan dari {a} + {b} adalah {a+b}')
    return a + b

def perkurangan():
    print('Anda memilih operasi pengurangan')
    a = int(input('Masukkan angka pertama : '))
    b = int(input('Masukkan angka kedua : '))
    print(f'Hasil pengurangan dari {a} - {b} adalah {a - b}')
    return a - b

def perkalian():
    print('Anda memilih operasi perkalian')
    a = int(input('Masukkan angka pertama : '))
    b = int(input('Masukkan angka kedua : '))
    print(f'Hasil perkalian dari {a} x {b} adalah {a*b}')
    return a * b

def pembagian ():
    print('Anda memilih operasi pembagian')
    a = int(input('Masukkan angka pertama : '))
    b = int(input('Masukkan angka kedua : '))
    print(f'Hasil pembagian dari {a} : {b} adalah {a/b}')
    return a / b

def modulo ():
    print('Anda memilih operasi Modulo')
    a = int(input('Masukkan angka pertama : '))
    b = int(input('Masukkan angka kedua : '))
    print(f'Hasil modulo dari {a} mod {b} adalah {a%b}')
    return a % b

def pangkat ():
    print('Anda memilih operasi perpangkatan')
    a = int(input('Masukkan angka pertama : '))
    b = int(input('Masukkan angka kedua : '))
    print(f'Hasil perpangkatan dari {a} ** {b} adalah {pow(a,b)}')
    return pow(a,b)