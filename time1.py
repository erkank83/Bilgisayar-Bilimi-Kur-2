from time import perf_counter
print("Adınızı Giriniz: ", end="")
baslangicZamani = perf_counter()
ad = input()
bitisZamani = perf_counter()
print("{} bilgilerinizi {} zamanda girdiniz".format(ad,bitisZamani-baslangicZamani))

