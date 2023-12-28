#chuong 10
#10.1
a=eval(input('a='))
b=eval(input('b='))
c=eval(input('c='))
d=eval(input('d='))
numlist=[a,b,c,d]
print('Max', '=',max(numlist))
print('Min', '=',min(numlist))
#10.2
x=float(input("nhap gia tri x:"))
print("|x| =",abs(x))
#10.3
import math
x=int(input("nhap so x:"))
n=int(input("nhap so n:"))
S=math.pow(x**2 +1, n)
print("S=", S)
#10.4
import math
x=int(input("nhap so x:"))
n=int(input("nhap so n:"))
A=math.pow(x**2 + x + 1,n) + math.pow(x**2 -x+1,n)
print("A=",A)
#10.5
zip_code=input("nhap ma zip code:")
if len(zip_code)==6 and zip_code.isdigit():
    print("là mã zip cua Viet Nam")
else:
    print("khong la ma zip cua Viet Nam")
#10.6
import math
a=int(input("nhap so a:"))
b=int(input("nhap so b:"))
c=int(input("nhap so c:"))
delta=b**2 -4*a*c
if a==0:
    x=-c/b
    print("x=",x)
elif delta>0:
    x1=(-b +delta**0.5)/(2*a)
    x2=(-b -delta**0.5)/(2*a)
    print('x1=',x1)
    print('x2=',x2)
elif delta==0:
    x=-b/2*a
    print('x',x)
elif delta<0:
    print("phuong trinh vo nghoem")
#10.8
import calendar
ngay=input("nhap ngay:")
thang=input("nhap thang:")
nam=input("nhap nam")
print("ngay thang nam vua ngap",ngay,'-', thang,'-', nam)
print("thu", calendar.weekday(nam,thang,ngay))
print("so ngay cua thang",calendar.monthrange(nam,thang))


