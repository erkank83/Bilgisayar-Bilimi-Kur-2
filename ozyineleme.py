#Özyineleme ile faktöriyel hesaplama
def faktoriyel(n):
#Gelen n değerinin faktöriyeli alır.
    if n==0:
        return 1
    else:
        return n*faktoriyel(n-1)
def main():
    # Fonksiyonumuza çeşitli değerler ile test edelim
    print(" 0! = ", faktoriyel(0))
    print(" 1! = ", faktoriyel(1))
    print(" 6! = ", faktoriyel(6))
    print("10! = ", faktoriyel(10))
main()
