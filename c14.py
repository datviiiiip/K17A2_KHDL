#chuong 14
#1
def kiem_tra_tam_giac(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    return False

def nhap_do_dai_canh():
    try:
        a=float(input("canh thu 1 cua tam giac"))
        b=float(input("canh thu 2 cua tam giav"))
        c=float(input("canh thu 3 cua tam giac"))
    except NameError as er1:
        print('Error : ', er1)
    except ZeroDivisionError as er2:
        print('Error : ', er2)
    if kiem_tra_tam_giac(a, b, c):
        print("thoa man dieu kien")
    else:
        print("khong thoa man dieu kien")
#2
danh_sach_so=[]
while True:
    try:
        so_duong=int(input("nhap so nguyen duong"))
        if so_duong==0:
            break
        if so_duong>0:
            danh_sach_so.append(so_duong)
    except ValueError:
        print("vui long nhap so nguyen hop le")
    except (NameError, ZeroDivisionError) as er:
        print("Error :", er)
    

