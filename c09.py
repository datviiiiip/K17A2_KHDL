#chuong9
#9.3
import math
def tinh_bmi(can_nang,chieu_cao):
    bmi=can_nang/math.pow(chieu_cao,2)
    return bmi
def danh_gia_bmi(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif 18.5<= bmi<=24.99:
        return "Bình thường"
    else:
        return "Thừa cân"
can_nang=float(input("nhap can nang:"))
chieu_cao=float(input("nhap chieu cao:"))
bmi = tinh_bmi(can_nang, chieu_cao)
print("danh gia:",danh_gia_bmi(bmi))
#9.4
def tinh_S(n,x):
    S=(x**2 +1)**n
    return S
n=int(input("nhap n:"))
x=int(input("nhap x:"))
print('s',tinh_S(n,x))
#9.5
def tinh_A(n,x):
    A=(x**2 +x+1)**n + (x**2 -x+1)**n
    return A
n=int(input("nhap n:"))
x=int(input("nhap x:"))
print("A",tinh_A(n,x))
#9.6
def so_nguyen_to(x):
    if x<2:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
so_can_kiem_tra=int(input("so can kiem tra"))
if so_nguyen_to(so_can_kiem_tra):
    print(so_can_kiem_tra,"la so nguyen to")
else:
    print(so_can_kiem_tra,"khong la so nguyen to")
#9.8
def so_hoan_hao(x):
    if x<0:
        return False
    tong=0
    for i in range(1,x):
        if x%i==0:
            tong+=i
        if tong==x:
            return True
so_can_kiem_tra=int(input("so can kiem tra"))
if so_hoan_hao(so_can_kiem_tra):
    print(so_can_kiem_tra,"la so hoan hao")
else:
    print(so_can_kiem_tra,"khong la so hoan hao")
#9.1
def sign(x):
    if x < 0:
        return
    elif x == 0:
        return
    else:
        return
#9.9
p=lambda a, b: 2*(a+b)
s=lambda a, b: a*b
a=int(input("chieu dai:"))
b=int(input("chieu rong:"))
S=s(a,b)
P=p(b,b)
print("chu vi hinh chu nhat:",P)
print("dien tich hinh chu nhat:",S)


    
        
        


    
