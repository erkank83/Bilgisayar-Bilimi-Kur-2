cumle=input("Bir cümle giriniz: ")
dizi=cumle.split()
for kelime in dizi:
   print(kelime[0], sep='', end='.', flush=True)
