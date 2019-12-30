deger = int(input("Lütfen 0 – 5 arasında bir değer girin: "))
cevap="aralıkta değil" #Varsayılan Cevap
if deger == 0:
    cevap="Sıfır"
elif deger == 1:
    cevap="Bir"
elif deger == 2:
    cevap="iki"
elif deger == 3:
    cevap="üç"
elif deger == 4:
    cevap="dört"
elif deger == 5:
    cevap="beş"
print("Girdiğiniz sayı",cevap)
    
