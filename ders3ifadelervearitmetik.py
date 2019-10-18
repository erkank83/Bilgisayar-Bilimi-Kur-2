#input():Klavyeden veri almak için kullanılır. str tipinde veri döndürür
print(type(input("Veri giriniz:")))
#10           -> <class 'str'>
#fen lisesi   -> <class 'str'>
#True         -> <class 'str'>
deger1=int(input("Bir sayı giriniz:"))#str veriyi int tipine döndürür deger1 değikenine atar.
deger2=int(input("Başka bir sayı giriniz:"))#str veriyi int tipine döndürür deger2 değikenine atar.
toplam=deger1+deger2 #deger1 ile deger2 toplanır toplam değişkenine atanır
print(deger1,"+",deger2,"=",toplam)# 10 + 20 = 30
x,y=5,6 #Eğer x ve y rakamsa, x, y’ye eklenir.
print(x,"+",y,"=",x+y)#5 + 6 = 11
x,y="Fen","Lisesi"
print(x,"+",y,"=",x+y)#Fen + Lisesi = FenLisesi
x,y=100.7,55.8 #Eğer x ve y sayı ise, x’ten y çıkarılır.
print(x,"-",y,"=",x-y)#100.7 - 55.8 = 44.900000000000006
x,y=2,3 #Eğer x ve y rakamsa, x ile y çarpılır.
print(x,"*",y,"=",x*y)#2 * 3 = 6
x,y="Fen",4 #Eğer x harf dizisi ise ve y rakamsa, x, y kez sıralanır.
print(x,"*",y,"=",x*y)#Fen * 4 = FenFenFenFen
x,y=3,"Lisesi"#Eğer x rakamsa ve y harf dizisi ise y, x kez sıralanır.
print(x,"*",y,"=",x*y)#3 * Lisesi = LisesiLisesiLisesi
x,y=4,6 #Eğer x ve y rakamsa, x, y’ye bölünür.
print(x,"/",y,"=",x/y)#4 / 6 = 0.6666666666666666
x,y=10,4#Eğer x ve y rakamsa, x’in içinde y değişkenin katsayısını arar.
print(x,"//",y,"=",x//y)#2 çıkar yani 10 içinde 4 iki kere tekrar eder
x,y=7,4#Eğer x ve y rakamsa, bölme işleminde x / y kalan kısmını verir.
print(x,"%",y,"=",x%y)#7 % 4 = 3
x=int(input("x:"))#x:2
y=int(input("y:"))#y:3
print(x,"**",y,"=",x**y)#2 ** 3 = 8
print(25//4, 4//25)#6 0 -> 25'in içinde 4, 6 kere tekrar eder ama 4'ün içinde 25 yoktur
#karışık türlü ifadeler
x=4# x tamsayı değeri içerir
y=10.2 #y ondalıklı sayı değeri içerir
print(x,"+",y,"=",x+y) #4 + 10.2 = 14.2   sonuç ondalıklı sayıdır.

