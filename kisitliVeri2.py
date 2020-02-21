def arasindaMi(ilk,son):
    deger=int(input("{} ile {} arasında bir değer giriniz :  ".format(ilk,son)))
    while deger < ilk or deger > son:
        deger=int(input("Tekrar deneyin!:"))
    return deger
def main():
    ilk=int(input("İlk değeri giriniz :"))
    son=int(input("Son değeri giriniz :"))
    sonuc=arasindaMi(ilk,son)
    print("Girmiş olduğunuz {}, {} ile {} aralığındadır".format(sonuc,ilk,son))
main()
