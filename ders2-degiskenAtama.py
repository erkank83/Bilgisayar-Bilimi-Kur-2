#Bir değişkene defalarca farklı değerler atayabiliriz. 
x=10
print(x)
x=20
print(x)
x=30
print(x)
# Bazı fonksiyonlar bir ya da daha fazla değişkene bağımlı hareket edebilir
x=10
print("x = "+str(x))
x=20
print("x = "+str(x))
x=30
print("x = "+str(x))
#print("x =", x) 
#İlk parametre “x =” dizisi ve ikinci parametre ise x değişkeni ile eşleşmiş değerdir
x, y, z = 100, -45, 0
print("x =", x, " y =", y, " z =", z)
x=2
y=5
x=3
x=y
y=7
print("x =",x,"y =",y)
#Programın çalışması sırasında bir değişkenin yalnızca değeri değil, türü de değişebilir.
a = 10
print("a değişkeninin ilk değeri", a, "ve tipi", type(a))
a = "ABC"
print("a değişkeninin yeni değeri", a, "ve tipi", type(a))
