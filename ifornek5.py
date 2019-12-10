#Mantıksal operatörlerden and ve or sola birleşmeli, not sağa birleşmelidir. Örneğin,
x,y=10,20
b = (x==10)#10==10-->True
print(b)# b’ye True değerini atar.
b = (x != 10)#10!=10-->False
print(b) # b’ye False değerini atar.
b = (x == 10 and y == 20)#(True and True)--> True
print(b)# b’ye True değerini atar.
b = (x != 10 and y == 20)#(False and True)--> False
print(b)# b’ye False değerini atar.
b = (x == 10 and y != 20)#(True and False)--> False
print(b)# b’ye False değerini atar.
b = (x != 10 and y != 20)#(False and False)--> False
print(b)# b’ye False değerini atar.
b = (x == 10 or y == 20) #(True or True)--> True
print(b)# b’ye True değerini atar.
b = (x != 10 or y == 20) #(False or True)--> True
print(b)# b’ye True değerini atar.
b = (x == 10 or y != 20) #(True or False)--> True
print(b)# b’ye True değerini atar.
b = (x != 10 or y != 20) #(False or False)--> False
print(b)# b’ye False değerini atar.
