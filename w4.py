#Belirli döngü örneği 2
print("Belirli döngü örneği")
n = 1
karar= int(input("Üst sınırı giriniz :"))
while n <= karar:
    print(n,end=" ")
    n += 1
print("\nBelirsiz döngü örneği")
#Belirsiz döngü örneği 3
karar = False
while not karar:
    giris = int(input("Çıkmak için 999 basın :"))
    if giris == 999:
        karar = True
    else:
        print(giris)
