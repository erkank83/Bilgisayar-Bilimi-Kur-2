# tanımlanmış bir değişkeni tanımsız bir değişkene dönüştürmek isteriz.
# Bu işlemi del satırını kullanarak gerçekleştiririz.
x=2
print("x=",x)# 2
a,b,c=0,1,2
print("a=",a,"b=",b,"c=",c)# a= 0 b= 1 c= 2
del x   # x değişkenini tanımsız hale getiriyoruz
print(x)
del a,b,c #toplu olarak tanımsız değişken yapıyoruz
print("a=",a,"b=",b,"c=",c)
