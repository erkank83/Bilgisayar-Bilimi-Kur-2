#Dışarıdan N/n karakteri girilinceye kadar
#döngünün kaç kere döndüğünü ekrana yazan while döngüsü
sayac=0
karakter="Y"
while karakter!='n' and karakter!='N':
    karakter=input("Devam için  (Y)\nÇıkmak için (N) harfine basınız:")
    if karakter=="Y" or karakter=="y":
        sayac+=1
    elif karakter!='n' and karakter!='N':
        print("(" + karakter + ") geçerli bir giriş kodu değil")
    print(sayac)
