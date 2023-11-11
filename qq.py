#chuong 6
#1.4
#1
print("{0} 5-3 {1} // 2".format("(", ")"))
#2
print("8 - {0} 3*2 {1} - {2} 1+1 {3}".format("(", ")", "(", ")"))
#1.5
so_luong=eval(input("so luong"))
don_gia=eval(input("don gia"))
thanh_tien=so_luong * don_gia
print('nhap so luong:',so_luong)
print('nhap don gia:',don_gia)
print('thanh tien', '=', so_luong, '*', don_gia, '=',thanh_tien)
#1.7
do_c=float(input("do C:"))
do_f=9/5 * do_c +32
print('nhap do c:',do_c)
print(do_c, 'do c', '=', do_f, 'do f')
#1.8
chuoi_s1=input("chuoi s1")
chuoi_s2=input("chuoi s2")
chuoi_s3=input("chuoi s3")
index=eval(input("index:"))
print('nhap chuoi s1:',chuoi_s1)
print('nhap chuoi s2:',chuoi_s2)
print('nhap chuoi s3:',chuoi_s3)
print('nhap index:',index)
print('chieu dai chuoi s1', '=',len(chuoi_s1))
print('chieu dai chuoi s2', '=',len(chuoi_s2))
print('chieu dai chuoi s3', '=',len(chuoi_s3))
print('chuoi s4', '=',chuoi_s1[index:5])
print('chuoi s2 lap lai 2 lan', '=',chuoi_s2*2)
#1.9
Lai_suat_mot_nam=float(input("lai suat mot nam"))
So_tien_gui=float(input("so tien gui"))
So_thang_gui=float(input("so thang gui"))
Tien_lai=(So_tien_gui*So_thang_gui)*(Lai_suat_mot_nam/100/12)
Tong_so_tien=So_tien_gui+Tien_lai
print('Lai suat 1 nam (%):',Lai_suat_mot_nam)
print('So tien gui:',So_tien_gui)
print('So thang gui:',So_thang_gui)
print('Tien lai', '=',Tien_lai)
print('tien von', '+', 'Lai', '=', So_tien_gui, '+', Tien_lai, '=',Tong_so_tien)
#1.6
alice_candies=eval(input('keo cua alice'))
bob_candies=eval(input('keo cua bob'))
carol_candies=eval(input('keo cua carol'))
so_keo_du=(alice_candies+bob_candies+carol_candies)%3
print('so keo can dap',so_keo_du)
