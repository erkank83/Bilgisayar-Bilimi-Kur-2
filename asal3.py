from math import sqrt
def asal(n):
    kok=round(sqrt(n))+1
    for deneme in range(2,kok):
        if n % deneme==0:
            return False
        else:
            return True
def main():
    en_buyuk=int(input("Asal sayıları hangi değere kadar gösterelim? "))
    for deger in range(2,en_buyuk+1):
        if asal(deger):
            print(deger,end=" ")
    print()
main()
