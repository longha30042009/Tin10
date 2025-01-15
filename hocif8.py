#Cho 3 so  nguyen duong khac 0 in ra man hinh so la thuong cua 2 so con lai
#vd a=3
#b=9
#c=21
#kq= a la thuong cua b va c vi 9%3 va 21%3

#vd
#a=5
#b=7
#c=15
#kq= ko ton tai gia tri

#input: 3 so nguyen duong != 0 hien ra man hinh thuong cua 2 so con lai
#output: b%a  and c%a a la thuong
#        a%b  and c%b b la thuong
#        a%c  and b%c c la thuong

def timthuong(a,b,c ):
    if (b%a==0  and c%a==0) or (a%b==0  and c%b==0) or (a%c==0 and b%c==0):
        if b%a==0  and c%a==0:
             print("a la thuong cua b va c vi ",b,"%",a,"va",c,"%",a)
        elif a%b==0  and c%b==0:
            print("b la thuong cua a va c vi ",a,"%",b,"va",c,"%",b) 
        else:
            print("c la thuong cua a va b vi ",a,"%",c,"va",b,"%",c)  
    else:
        print("ko ton tai gia tri")         


# a=int(input("so   "))      
# b=int(input("so   "))     
# c=int(input("so   "))


a=15
b=5
c=10

timthuong(a,b,c)


#vd
#a=15
# b=5
# c=10
# timthuong(15,5,10)
#if (5%15==0  and 10%15==0)(F) or (15%5==0  and 10%5==0)(T) or (15%10==0 and 5%10==0):(F)  => T
        # elif 15%5==0(T)  and 10%5==0:(T) =>(T)
        #     print("b la thuong cua a va c vi ",15,"%",5,"va",10,"%",5) 