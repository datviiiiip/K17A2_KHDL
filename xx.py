#chuong 8
#8.1
a=eval(input('a='))
b=eval(input('b='))
c=eval(input('c='))
d=eval(input('d='))
numlist=[a,b,c,d]
print('Max', '=',max(numlist))
print('Min', '=',min(numlist))
#8.2
x=eval(input('nhap x:'))
if x < 0:
    print('|', x, '|', '=',x*-1)
else:
    print('|', x, '|', '=',x*1)
#8.3
a=eval(input('a:'))
b=eval(input('b:'))
if a == 0:
    print('hu cau')
else:
    x=-b/a
    print('phuong trinh bac nhat:',a, 'x', '+',b)
    print('x', '=',x)
#8.4
import math
a=float(input('canh a:'))
b=float(input('canh b:'))
c=float(input('canh c:'))
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print('dien tich cua tam giac:',s)
#8.5
x=eval(input('nam nhap vao'))
if (x%400 == 0) or (x%4 == 0) and (x%100 != 0):
    print('Nam', x, 'la nam nhuan')
else:
    print('Nam', x, 'la nam khong nhuan')
#8.6
loai_xe=float(input('nhap loai xe:'))
so_km=float(input('nhap so km:'))
thoi_gian_cho=float(input('nhap thoi gian cho:'))
if thoi_gian_cho > 5:
    tien_cho=(thoi_gian_cho -5)*800
    print('tien cho:',tien_cho)
else:
    tien_cho=0
    print('tien cho:',tien_cho)
if loai_xe==4 or loai_xe==7:
    if loai_xe==4:
        if so_km <= 20:
            tien_di_chuyen=so_km*12.100
            print('tien di chuyen:',tien_di_chuyen)
        else:
            tien_di_chuyen=(20*12.100)+(so_km-20)*10.000
            print('tien di chuyen:',tien_di_chuyen)
    if loai_xe==7:
        if so_km <= 30:
            tien_di_chuyen=so_km*14.100
            print('tien di chuyen:',tien_di_chuyen)
        else:
            tien_di_chuyen=(30*14.100)+(so_km-30)*12.000
            print('tien di chuyen:',tien_di_chuyen)
    tien_cuoc=tien_cho+tien_di_chuyen
    print('tien cuoc:',tien_cuoc)
else:
    print('khong có dich vu')
#8.7
so_kwh=eval(input('so kwh'))
if so_kwh>=401:
    tien_dien=50*1678+50*1734+100*2014+100*2536+100*2834+(so_kwh-40)*2927
    print('tien dien',tien_dien)
elif so_kwh>=301:
    tien_dien=50*1678+50*1734+100*2014+100*2536+(so_kwh-300)*2834
    print('tien dien',tien_dien)
elif so_kwh>=201:
    tien_dien=50*1678+50*1734+100*2014+(so_kwh-200)*2536
    print('tien dien',tien_dien)
elif so_kwh>=101:
    tien_dien=50*1678+50*1734+(so_kwh-100)*2014
    print('tien dien',tien_dien)
elif so_kwh>=51:
    tien_dien=50*1678+(so_kwh-50)*1734
    print('tien dien',tien_dien)
else:
    tien_dien=so_kwh*1678
    print('tien dien',tien_dien)
#8.9
n=int(input('n='))
while n>0:
    print(n)
    n-=1
print('start')
#8.10
n=int(input('so nguyen'))
x=float(input('so thuc'))
s=(x**x + 1)**n
print('nhap n:',n)
print('nhap x:',x)
print('A=',s)
#8.11
n=int(input('nhap so nguyen'))
x=float(input('nhap so thuc'))
a=(x**x + x + 1)**n + (x**x - x + 1)**n
print('nhap n:',n)
print('nhap x:',x)
print('A=',a)

    
