a,b,c,d=1,2,3,4
print(not (a == b and c != d))      #not(False and True)-> True
print(not (a == b and not (c == d)))#not( False and True)->True
print(not (a == b) or not (c != d)) #not( False) or not( True)->True or False->True
print(a != b or c == d)             #True or False -> True
