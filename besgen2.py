# turtle modülünü kullanarak beşgen çizimi
import turtle
import time
# turtle modülü programa ekleniyor
def polygon(sides,length,x,y,color):
    #polygon adında ve içerisine 5 değer alabilen bir fonksiyon tanımlanıyor
    turtle.penup()
    # Çizimi yapacak kalemin yönleri belirleniyor
    turtle.setposition(x,y)
    # Parametre olarak gelen x,y değerleri başlangıç noktası olarak belirleniyor
    turtle.pendown()
    # Çizimi yapacak kalemin yönleri belirleniyor
    turtle.color(color)
    # Parametre olarak gelen renk atanıyor
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(length)
        turtle.left(360//sides)
        turtle.end_fill()

def veriGirisi():
    #veriGirişi adında bir fonksiyon tanımlanıyor
    try:
        sides=int(input("Kaç kenar olsun :"))
        length=int(input("Kenar uzunlarını giriniz :"))
        x=int(input("x :"))
        y=int(input("y :"))
        color=input("Renk :")
        polygon(sides,length,x,y,color) # Tanımlanan fonksiyonun istenilen parametrelerle çağırılması
        return True
    except ValueError:
        print("Geçeriz veri girişi")
#Ana fonksiyon
print("Çıkmak için x tuşuna basın!",end=" ")
tus=input()
if tus=="x" or tus=="X":
    pass
else:
    while True:
        if veriGirisi()==True:
            break
        else:
            veriGirisi()            
time.sleep(5)#konsol ekranından çalıştırıldığında 5 sn bekletir
