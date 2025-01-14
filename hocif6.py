#Cho hai so a va b nguyen duong chac chan 1 so la thang,nam, ktra 1 trong 2 co the la so thang hoac so nam phan biet so nao la thang so nao la nam
#vd:
#a=19
#b=7
#kq= a la nam 
#     b la thang
# a=12
#b=100
#kq= a la thang 
#  b la nam

def thangnam(a,b):
        if a<b:
            print("a la thang ")
            print("b la nam")
        else:
            print("a la nam ")
            print("b la thang")
    
# a=int(input("so  "))            
# b=int(input("so  "))  
 





#de2  them so c phan biet ngay thang nam cua ba so a,b,c ngay so the trung vs thang  nam luon >31
#vd
#a=100
#b=12
#c=12
#kq= a la nam
     #b la thang  hoac ngay
     #c la thang hoac ngay

#vd
# a=7
# b=20
# c=50
#    kq=  a la thang
# b  la ngay
# c  la nam

def ngaythangnam(a,b,c):
        if a>b and a>c:
            print("a la nam ")
            if b<c:
                print("b la thang")
                print("c la  ngay")
            else:
                print("b la ngay")
                print("c la thang")   
        elif b>a and b>c:
            print(" b la nam")
            if a<c:
                 print("a la thang")
                 print("c la ngay")
            else:
                 print("a la ngay")  
                 print("c la thang ")
        else:
            print("c la nam")
            if b<a:
                  print("a la ngay")
                  print("b la thang")
            else:
                 print("a la thang")
                 print("b la ngay")



            
    
# a=int(input("so  "))            
# b=int(input("so  "))  
# c=int(input("so  "))  


a=1000
b=31
c=12

ngaythangnam(a,b,c)

