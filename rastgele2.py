from random import randrange, seed, choice
#randrange: Belirli bir aralıkta sözde rastgele tam sayı bir değer döndürür.
for i in range(0, 100): # 100 adet rastgele sayı için döngü kuruluyor
    print(randrange(1, 1001), end=" ") # 1..1001 aralığında üretilen rastgele sayı yazdırılıyor
#seed: Rastgele değer dizisi için bir değer alır.
#choice: Değerler arasından rastgele bir değer seçer.
