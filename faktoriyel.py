# Program girilen sayının faktöriyelini hesaplar
faktoriyel=1
sayac=1
sayi=int(input("Lütfen bir sayı giriniz.."))
while sayac<=sayi:
    faktoriyel*=sayac
    sayac+=1
print(sayi," sayısının foktöriyeli:",faktoriyel)
