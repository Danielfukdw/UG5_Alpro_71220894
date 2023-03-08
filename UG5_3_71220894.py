import math

jarak_awal = input('Masukan jarak awal (dalam meter) :')
sudutPertama = int(input('Masukan sudut elevasi pada menit ke-5 (dalam derajat): '))
sudutDua = int(input('Masukan sudut elevasi pada menit ke-6 (dalam derajat): '))
tinggi_heli = int(jarak_awal) * math.tan(sudutPertama)
jarakAkhir = int(jarak_awal) * math.tan(sudutDua) - math.tan(sudutPertama)
Selisih_tinggi = jarakAkhir * math.tan(sudutDua)
program = 0

while jarak_awal.lower != ("stop", 'berhenti'):
    print(tinggi_heli)
    print(jarakAkhir)
    print(Selisih_tinggi)
else:
    print('Program dihentikan')

# jarak_awal != ("stop", 'berhenti'):
#         program + 1
#         print (tinggi_heli)
#         print (jarakAkhir)
#         print (Selisih_tinggi)
# else :
#         print('Program dihentikan')