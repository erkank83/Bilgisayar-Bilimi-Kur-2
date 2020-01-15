# Metin içerisindeki sesli harfleri bulma krana yazan program
kelime = input("Lütfen bir metin giriniz (Çıkış için X / x): ")
sesliHarfSayisi = 0
for c in kelime:
    if c == "A" or c == "a" or c == "E" or c == "e" \
    or c == "I" or c == "ı" or c == "O" or c == "o"\
    or c == "U" or c == "u" or c == "Ö" or c == "ö"\
    or c == "Ü" or c == "ü" or c == "İ" or c=="i":
        print(c, ",", end=" ", sep=" ")
        sesliHarfSayisi += 1
    elif c == "X" or c =="x":
        print("\nÇıkış yaptınız")
        break
print(" (", sesliHarfSayisi, " adet sesli harf)", sep="")
