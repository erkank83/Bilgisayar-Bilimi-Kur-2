# Bu program sqrt() fonksiyonunun farklı kullanımlarını gösterir.
from math import sqrt
x = 16
# İstenilen sabit değerin karekökünün alınması
print(sqrt(16.0))
# Değişkenin karekökünün alınmasını sağlar
print(sqrt(x))
# sqrt() fonksiyonunun içerisinde işlem kullanımı
print(sqrt(2 * x - 5))
# İşlem sonucu geri dönen değerin değişkene aktarılması
y = sqrt(x)
print(y)
# İçerisinde işlem kullanılan sqrt() fonksiyonunun dönen değerinin işleme tabi tutulması
y = 2 * sqrt(x + 16) - 4
print(y)
# İç içe sqrt() fonksiyonunun kullanılması
y = sqrt(sqrt(256.0))
print(y)
print(sqrt(int("45")))
