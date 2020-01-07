sayi = int(input("Lütfen tablo ölçülerini giriniz:"))
print(" ",end=" ")
for sutun in range(1, sayi + 1):
    print(" {0:3}".format(sutun), end="")
print()
print("  +", end=" ")
for sutun in range(1, sayi + 1):
    print("---", end=" ")
print()
for satir in range(1, sayi + 1):
    print("{0:2}|".format(satir), end=" ")
    for sutun in range(1, sayi + 1):
        deger = satir*sutun # Çarpım sonucunun hesaplanması
        print("{0:3}".format(deger), end=" ")
    print()
