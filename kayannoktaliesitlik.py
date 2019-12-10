d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print("d1 =", d1, "\nd2 =", d2)
if d1 == d2:
    print("Aynı")
else:
    print("Farklı")

if round(d1,2)==round(d2,2):
    print("Yuvarlanmış haller eşit",round(d1,2),"=",round(d2,2))
