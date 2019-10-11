#Ondalıklı sayılar için float tipi vardır
x=3.14
print(x)#3.14
print(type(x))#<class 'float'>
# Python ile kod yazarken 6.022 x 1023 yerine 6.022e23 olarak yazmamız gerekir
x=10e2#e'nin solundaki sayı aynen kalır ve e'nin sağındaki sayı kadar 0 eklenir
print("x =",x)#x = 1000.0
print(type(x))#<class 'float'>
#Yuvarlama: Reel sayıya en yakın tam sayıya ulaşmak için kesrin belirli bir miktarı eklenerek ya da
#çıkarılarak yuvarlama yapılır
#Kesme: Sayının kesirli kısmı tamamen göz ardı edilir.
print(int(28.71))#28
print(round(28.71))#29
print(round(19.47))#19
print(int(19.47))#19
x=93.34836
print(x)#93.34836
print(round(x))#93-> .dan sonraki sayi 5'ten küçük olduğundan yukarı yuvarlama olmaz
print(round(x,2))#93.35 ->34'ten sonra 8 geldiğinden yukarı yuvarlar 35 olur.
print(round(x,3))#93.348->348'den sonra 3 geldiğinden yuvarlama olmaz.
print(round(x,0))#93.0
print(round(x, 1))#93.3-> 3'ten sonra gelen 4, 5'ten küçük olduğundan yuvarlama olmaz
print(type(round(x)))#<class 'int'>
print(type(round(x,1)))#<class 'float'> Ondalıklı hale gelir
print(type(round(x,2)))#<class 'float'> Ondalıklı hale gelir
x = 28793.54836
print(round(x))   #28794      --> 3.5 bir fazlaya yuvarlandı 4 oldu
print(round(x,0)) #28794.0    -->  iki parametre ondalıklı hale dönüştürdü
print(round(x,1)) #28793.5    --> .54 ifadesinde 4, 5'ten küçük olduğundan yuvarlama yok
print(round(x,2)) #28793.55   --> .548 ifadesinde 8, 5'ten büyük olduğundan yuvarlama var
print(round(x,-1))#28790.0    --> 3, 5'ten küçük olduğundan sola yuvarlama yok basamak sayısına 0 gelir
print(round(x,-2))#28800.0    --> 9, 5'ten büyük olduğundan sola yuvarlama var 2tane 0 var  
y=65535
print(round(y))   #65535      --> Sağa yuvarlanacak kesirli ifade yok
print(round(y,0)) #65535      --> Sağa yuvarlanacak kesirli ifade yok
print(round(y,1)) #65535      --> Sağa yuvarlanacak kesirli ifade yok
print(round(y,2)) #65535      --> Sağa yuvarlanacak kesirli ifade yok
print(round(y,-1))#65540      --> 35'in 5'i 5'e eşit olduğundan sola yuvarlar 3'ü 4 yapar
print(round(y,-2))#65500      --> 53'ün 3'ü 5'ten küçük olduğundan sola yuvarlama yok 0 yazar
print(round(y,-3))#66000      --> 55'in 5'i 5'e eşit olduğunda sola yuvarlar 5'i 6 yapar
print(round(y,-4))#70000      --> 66'in 6'sı 5'ten büyük olduğundan sola yuvarlar ve 0 koyar 70 olur
print(round(y,-5))#100000     --> 5.basamaktaki 6, 5'ten büyük olduğundan sola bir ekler ve 0 yazar
print(round(y,-6))#0          --> 6.basamakta sayı olmadığından sadece 0 yazar
