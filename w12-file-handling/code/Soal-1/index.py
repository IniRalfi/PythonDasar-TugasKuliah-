d = open('Soal-1/data.txt', 'w')
d.write('Halo\n')
d.write('Teks ini akan muncul di file ini')
d.close

d= open('Soal-1/data.txt', 'r')
print(d.read())