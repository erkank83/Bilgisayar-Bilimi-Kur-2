#Yöntem 1
from time import perf_counter
from math import sqrt

def asalMi(n):
    sayac=0
    for i in range(1,n):
        if n%i==0:
            sayac+=1
    if sayac==1:
        return True
    else:
        return False

sonDeger = int(input("Kaça kadar asal sayıları görmek istersiniz? "))
s=2
adet=0
basla = perf_counter()# Süre başlatılıyor
while s<=sonDeger:
    if asalMi(s):
       adet+=1# print(s,end=" ")
    s+=1
gecenZaman = perf_counter() - basla # Geçen zaman hesaplanıyor
print("Yöntem1:\nAdet: {} Geçen Süre: {}".format(adet,gecenZaman))

#Yöntem 2
adet=0
deger = 2 # En küçük asal sayı
basla = perf_counter()# Süre başlatılıyor
while deger <= sonDeger:
    # İstenilen değere kadar dönmesi için döngü kuruluyor
    kontrol = True # Başlangıç aşamasında kontrol değişkeni True olarak belirlenir
    # 2 ile -1 arasındaki tüm değerlerin kontrolünün yapılması
    geciciDeger= 2
    kok = sqrt(deger) # Döngüde sırası gelen değerin karakökü hesaplanıyor
    while geciciDeger <= kok:
        if deger % geciciDeger == 0:
            kontrol = False # Asal sayı özelliği yitiriliyor ve kontrol False oluyor
            break # Kontrol döngüsünden çıkılıyor.
        geciciDeger += 1 # Bir sonraki kontrol sayısına geçiş
    if kontrol:
        adet+=1# adetler sayılıyor
    deger += 1 # Asal sayı kontrolü için sonraki sayı
gecenZaman = perf_counter() - basla # Geçen zaman hesaplanıyor
print("Yöntem2:\nAdet: {} Geçen Süre: {}".format(adet,gecenZaman))

