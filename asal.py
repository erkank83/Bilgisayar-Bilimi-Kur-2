def asalMi(n):
    sayac=0
    for i in range(1,n):
        if n%i==0:
            sayac+=1
    if sayac==1:
        return True
    else:
        return False

sonDeger = int(input("Kaça kadar asal sayıları görmek istersiniz? "))
s=2
while s<=sonDeger:
    if asalMi(s):
        print(s,end=" ")
    s+=1

