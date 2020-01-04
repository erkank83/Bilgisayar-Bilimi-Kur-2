#named indexes:
metin1 = "Okul adı : {okuladi}, yıl: {yil}".format(okuladi = "İbrahim Önal Fen Lisesi", yil = 2020)
#numbered indexes:
metin2 = "Okul adı : {0}, yıl: {1}".format("İbrahim Önal Fen Lisesi",2020)
#empty placeholders:
metin3 = "Okul adı : {}, yıl: {}".format("İbrahim Önal Fen Lisesi",2020)

print(metin1)
print(metin2)
print(metin3)
