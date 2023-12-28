#chuong 13
#10.1
file = input("Nhập tên tập tin: ")
f = open(file,'r')
a = f.read()
print("noi dung tap tin")
print(a)
f.close()
#10.2
file = input("Nhập tên tập tin: ")
f = open(file, 'r')
a = f.read()
character=len(a)
words=len(a.split())
print("noi dung tap tin",a)
print("character",character)
print("words",words)
#10.3
file = input("nhap ten tap tin:")
with open(file,'w') as f:
    a=f.read()
    b=input("nhap noi dung:")
    f.write(b)
with open(file,'r') as f:
    c=f.read()
    if c:
        choice=input("noi dung da ton tai nhan y de xoa")
        if choice=='y':
            d=input("nhap noi dung moi vao")
        f.write(d)
    else:
        d=input("nhap noi dung de ghi nao tap tin")
        f.write(d)
#11.4
file = input("Nhap ten tap tin:")
f = open(file,'w')
a = f.read()
b = input("nhap noi dung moi vao")
f.write(b)
with open(file,'r') as f:
    c=f.read()
    if c:
        choice = input("ban co muon nhap noi dung vào tap tin khong 1:có, 0:không")
        while choice==1:
            d=input("nhap noi dung moi")
            f.write(d)
            choice = input("ban co muon tiep tuc nhap noi dung vao tap tin khong 1:co, 0:khong")
    else:
        d = input("nhap noi dung de ghi vao tap tin")
        f.write(d)
#11.5
import csv
def read_csv_file(filename):
    f=open(filename)
    for i in csv.reader(f):
        print(i)
    f.close()
#11.6
import csv
def danh_sach_so_dien_thoai(ten_tap_tin,danh_sach_sdt):
    f=open(ten_tap_tin,'a',newline='')
    for i in danh_sach_sdt:
        csv.write(f).writerow(i)


             
