from time import perf_counter
toplam = 0 # Toplam değişkeni tanımlanıp ilk değer olarak 0 veriliyor
basla = perf_counter()
for n in range(1, 1000001):
    # Toplamı alınacak sayılar için 1.000.000’e kadar döngü kuruluyor
    toplam += n
gecenZaman = perf_counter() - basla # Geçen zaman hesaplanıyor
print("Toplam: {} Geçen Süre: {}".format(toplam,gecenZaman))
