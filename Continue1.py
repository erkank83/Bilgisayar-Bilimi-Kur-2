# 999 girilene kadar girilen pozitif sayıların toplamını alan program
# < girilen negatif sayılar işleme alınmayacaktır. >
toplam = 0
durum = False
while not durum:
    deger = int(input("Lütfen pozitif tam sayı giriniz (Çıkış için 999):"))
    if deger < 0:
        print("Negatif değer girildi, ", deger, "degeri işleme alınmadı")
        continue
    if deger != 999:
        print("Eklenen değer", deger)
        toplam += deger
    else:
        durum = (deger == 999)
print("Toplam =", toplam)
