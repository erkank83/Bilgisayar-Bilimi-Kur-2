#Örnek: Kullanıcının girdiği saniyeleri, saat, dakika ve saniye olarak parçalara
#ayıran programda tamsayı bölme ve modül kullanır.
#çözüm 1
girilenSaniye = int (input ("Saniye sayısını girin:"))
saat = girilenSaniye // 3600 # 3600 saniye = 1 saat
dakika=girilenSaniye-saat*3600
dakika=(girilenSaniye//60) % 60
saniye=(girilenSaniye-dakika*60)%60
print(saat,"sa",dakika,"dk",saniye,"sn")
#çözüm 2
saniye = int (input ("saniye sayısını girin:"))
saat = saniye // 3600 # 3600 saniye = 1 saat
saniye = saniye% 3600
dakika = saniye // 60 # 60 saniye = 1 dakika
saniye = saniye% 60
print (saat, "sa", dakika, "dk", saniye, "sn")

