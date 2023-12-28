#chuong_11
#11.1
a=[1,2,3]
b=[1,[2,3]]
c=[]
d=[1,2,3][1:]
print("chieu dai danh sach a",len(a))
print("chieu dai danh sach b",len(b))
print("chieu dai danh sach c",len(c))
print("chieu dai danh sach d",len(d))
#11.3
animals=['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat','hippo']
print("Danh sách các con thú:",animals)
print("tong cac con thu",len(animals))
thu_can_tim=input("nhap so can tim:")
find=thu_can_tim in animals
if find:
    print(thu_can_tim, "có trong vuon")
else:
    print(thu_can_tim, "khong ton tai")
#11.6
chieu_cao=[74,74,72,72,73,69,69,71,76,71]
print("ba so dau tien",chieu_cao[0:3])
print("ba so cuoi cung",chieu_cao[7:10])         
print("chieu cao trung binh",sum(chieu_cao)/len(chieu_cao))
print("chieu cao lon nhat", max(chieu_cao))
print("chieu cao nho nhat", min(chieu_cao))
chieu_cao.sort()
print("chieu cao tang dan",chieu_cao)
chieu_cao.reverse()
print("chieu cao giam dan",chieu_cao)
#11.11
Tuple=('red','greem','yellow','blue','black','white','pink','orange','red','blue')
x=float(input("nhap so tu 0 den 9:"))
y=float(input("nhap so tu -1 den -9:"))
z=input("nhap chuoi can tim")
print("Tuple", "[", x,"]",Tuple[x])
print("Tuple", "[", y,"]",Tuple[y])
print(z, "xuat hien trong Tuple ",Tuple.count(z))
#11.11
import random
tuple_1 = tuple(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10))
print(tuple_1)
x=float(input("nhap so tu 0 den 9:"))
y=float(input("nhap so tu -1 den -9:"))
z=input("nhap chuoi can tim")
print("Tuple", "[", x,"]",Tuple[x])
print("Tuple", "[", y,"]",Tuple[y])
print(z, "xuat hien trong Tuple ",Tuple.count(z))
#11.12
tuple_a=(1,2,3,4)
tuple_b=(5,6,7,8)
tuple_c=tuple_a+tuple_b
tuple_d=tuple(sorted(c))
print("tuple a:",tuple_a)
print("tuple b:",tuple_b)
print("tuple c:",tuple_c)
print("tuple d:",tuple_d)
