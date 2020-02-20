# Girilen 2 sayıdan en büyük ortak bölen program
def gcd(s1,s2):
    min= (s1 if s1<s2 else s2)
    ebop=1
    for i in range(1,min+1):
        if s1%i==0 and s2%i==0:
            ebop=i # En büyük ortak bölen aktarılıyor
    return ebop

sayi1=int(input("Lütfen ilk sayıyı giriniz: "))
sayi2=int(input("Lütfen ikinci sayıyı giriniz: "))
sonuc=gcd(sayi1,sayi2)
print("En büyük ortak çarpan : {}".format(sonuc))
