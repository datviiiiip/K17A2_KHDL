#chuong 9
#9.1
def sign(x):
    if x==0:
        print('0,neu x la 0')
        return
    if x>0:
        print('1,neu x la so duong')
    else:
        print('-1,neu x la so am')
        return
#9.2
a= ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
b= ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]   
def nhap_nam(x):
    if x>0:
        if x%10==0:
        a="canh"
        elif x%10==1
        a="tan"
        elif x%10==2
        a="nham"
        elif x%10==3
        a="quy"
        elif x%10==4
        a="giap"
        elif x%10==5
        a="at"
        elif x%10==6
        a="binh"
        elif x%10==7
        a="dinh"
        elif x%10==8
        a="mau"
        elif x%10==9
        a="ky"
    else:
        print('khong thoa man')
        return
    if x>0:
        if x%12==0
        chi_nam=than
        elif x%12==1
        chi_nam=dau
        elif x%12==2
        chi_nam=tuat
        elif x%12==3
        chi_nam=hoi
        elif x%12==4
        chi_nam=ty
        elif x%12==5
        chi_nam=suu
        elif x%12==6
        chi_nam=dan
        elif x%12==7
        chi_nam=mao
        elif x%12==8
        chi_nam=thin
        elif x%12==9
        chi_nam=ty
        elif x%12==10
        chi_nam=ngo
        elif x%12==11
        chi_nam=mui
    else:
        print('khong thoa man')
        return
    print('nam', x, 'lich am la nam', can_nam chi_nam)
     
