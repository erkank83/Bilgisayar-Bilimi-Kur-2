# Sıcaklık değerini okumak için
dereceF=float(input("Sıcaklığını F derece olarak girin:"))
#°C = (°F – 32) / 1.8
dereceC=(dereceF-32)/(9/5)
# Sonucu bildir
print (dereceF, "derece F =", dereceC, "C derece")
