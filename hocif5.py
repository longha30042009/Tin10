#  Cho 3 so,  co 1 so la hieu cua 2 so con lai thi in ra man hinh ct tinh cua no neu ko co ton tai thi hien ra man hinh ko ton tai
# vd 1,7,8 =>  in ra 8-1=7
# vd 1,7,9 => kq ko ton tai
# vd 12,14,2=> in ra 14-12=2
# vd 9,11,-2=> in ra 9-11=-2

def tinhhieu(a,b,c):
    if (-1000<=a<=1000)and(-1000<b<=1000)and(-1000<c<1000):
        if a-b==c:
            print(a,"-",b,"=",c)
        elif c-a==b:
            print(c,"-",a,"=",b) 
        elif b-c==a:
            print(b,"-",c,"=",a)
        else:
            print(" ket qua ko ton tai")

    else:
        print("so ko hop le")

    
    print("cuoiham")


# a=int(input("so  "))            
# b=int(input("so  "))  
# c=int(input("so  "))  

a=-2000
b=8
c=10

tinhhieu(a,b,c)

#lan2
#a=1
#b=7
#c=9
#if (-1000<=1<=1000)and(-1000<7<=1000)and(-1000<9<1000): (T,T,T)
#if 1-7==9:(F)
#print(1,"-",7,"=",9)(F)
#elif 9-1==7:(F)
#print(9,"-",1,"=",7) (F)
#else:
#print(7,"-",9,"=",1)(F)
#else:
        #print("ket qua ko ton tai") 
#kq= ket qua ko ton tai
      



#lan1
#a=1
#b=7
#c=8
#(-1000<=1<=1000)and(-1000<7<=1000)and(-1000<8<1000):( T, T, T)
#if 1-7==8:
            #print(1,"-",7,"=",8) (F)
#if 8-1==7:
            #print(8,"-",1,"=",7) (T)          
    #kq= 8-1=7