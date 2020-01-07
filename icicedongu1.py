# Hem satır hem de sütun oluşturmak için :
satirsayisi = int(input("Tablonun satır sayısını giriniz: "))
sutunsayisi = int(input("Tablonun sütun sayısını giriniz: "))
for satir in range(1,satirsayisi+1):
    for sutun in range(1,sutunsayisi+1):
        print("[{0:2},{1:2}]".format(satir,sutun),sep="",end=" ")
    print(end="\n")




