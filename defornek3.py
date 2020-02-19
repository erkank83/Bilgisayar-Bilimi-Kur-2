#çözüm 1
def say():
    for i in range(1, 11):
        print(i, end=" ")
    print()
print("10'a kadar sayılıyor. . .")
say()
print("Tekrar 10'a kadar sayılıyor. . .")
say()

#çözüm 2
def baslikYaz(sayi,sayac):
    print("{}.defa, {}'a kadar sayılıyor...".format(sayac,sayi))
    return sayac+1

def hesapla(sayi):
    for i in range(1,sayi+1):
        print(i,end=" ")
    print()#fonksiyon tekrar çağrıldığında alt satıra geç

def oku():
    sayi=int(input("Kaça kadar sayılmasını istiyorsun ?:"))
    return sayi
#Ana fonksiyon kısmı
sayac=1
sayi  = oku()
sayac = baslikYaz(sayi,sayac)
hesapla(sayi)
sayac = baslikYaz(sayi,sayac)
hesapla(sayi)



