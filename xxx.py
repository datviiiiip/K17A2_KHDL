#chuong 7
#7.1
x=float(input('x='))
S=(1 + x + x**3/3 + x**5/5)
print('1 + x+x^3/3 + x^5/5', '=',S)
#7.7
So_tien_muon_doi=eval(input('So tien muon doi'))
so_to_500000=So_tien_muon_doi//500000
tien_con_lai=So_tien_muon_doi%500000
so_to_200000=tien_con_lai//200000
tien_con_lai1=tien_con_lai%200000
so_to_100000=tien_con_lai1//100000
tien_con_lai2=tien_con_lai1%100000
so_to_50000=tien_con_lai2//50000
tien_con_lai3=tien_con_lai2%50000
print('so tien muon doi:',So_tien_muon_doi)
print('so to 500000:',so_to_500000)
print('so to 200000:',so_to_200000)
print('so to 100000:',so_to_100000)
print('so to 50000:',so_to_50000)
print('tien con lai:',tien_con_lai3)
#7.6
x=True
y=False
print('x and y :',x and y)
print('x of y :',x or y)
print('not x :',not x)
print('x is y :', x is y)
print('x is not y :', x is not y)
#7.5
x=15
y=12
print('Binary of x =', bin(x), ', Binary of y =', bin(y))
print('x & y =', bin(x & y))
print('x / y =', bin(x | y))
print('x ^ y =', bin(x ^ y))
print('~x =', bin(~x))
print('x << 2 =', bin(x << 2))
print('x >> 2 =', bin(y >> 2))
