#type():Verilen paramterenin tipini gösterir. Yorumlayıcı satırında
#doğrudan çalışırken ayrı sayfada print ile birlikte kullanmak gerekir.
print(type("5")) # "5" tırnak içinde olduğu için karakterdir
#<class 'str'>
print(type(5))   # 5 tırnaksız olduğu için sayıdır.
#<class 'int'>
print(type(False))# False,True mantıksal ifadelerdir.
#<class 'bool'>
print(type(3.14)) #3.14 ifadesi ondalıklı bir sayıdır.
#<class 'float'>
print(type(4+7)) # 4 bir tamsayıdır ve 7 de bir tamsayıdır. int+int->int
#<class 'int'>
print(type("4"+"7"))# "4" karakterdir ve "7" de karakterdir. str+str->str
#<class 'str'>
print( type(int("3") + int(4)))# "3" karakter iken int() fonksiyonu ile tamsayı olur
#4 tamsayı iken int() fonksiyonu ile tamsayı olur. int+int->int
#<class 'int'>
