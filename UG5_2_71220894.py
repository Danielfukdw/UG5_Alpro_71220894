def hitung_mobil():
    if daerah == "jogja":
        jumlahJog + 1
    elif daerah == "solo":
        jumlahSol + 1
    elif daerah == "magelang":
        jumlahMag + 1
    elif daerah == "surabaya":
        jumlahSur + 1
#     while daerah == "done":
    while True:
        print(jumlahJog)
        print(jumlahMag)
        print(jumlahSol)
        print(jumlahSur)
        break
    else:
        False
        

daerah = str(input('Masukan asal mobil (Ketik "done" untuk keluar) :')).lower
jumlah = int(input('Jumlah Mobil %s  :' % daerah))
jumlahJog = 0
jumlahSol = 0
jumlahSur = 0
jumlahMag = 0
