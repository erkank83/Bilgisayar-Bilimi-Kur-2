print("Yardım Edin! Bilgisayarım Çalışmıyor")
cozum = False
while not cozum:
    print("Bilgisayardan herhangi bir ses geliyor mu (fans vb) ")
    secim = input("Veya herhangi bir ışık yanıyor mu? (y/n):")
    if secim == "n":
        secim = input("Fişe takılı mı (y/n):")
        if secim == "n":
            print("Fişe takın")
        else:
            secim = input("Açma düğmesine bastınız mı (y/n):")
            if secim == "n":
                print("Açma düğmesine basın.")
            else:
                secim = input("Sigorta atmış mı? (y/n):")
                if secim == "n":
                    secim = input("Şalter inmiş mi (y/n):")
                    if secim == "n":
                        print("Şalteri kontrol edin veya yenisi ile değiştirin. ")
                    else:
                        print("Teknik servise başvurun.")
                    cozum = True
                else:
                    print("Sigortayı kontrol edin. ")
    else:
        print("Teknik servise başvurun...")
        cozum = True
                    
