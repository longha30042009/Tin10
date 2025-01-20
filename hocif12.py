#Cho2 so chac chan 1 so le va chac chan 1 so chan neu la so chan /2   neu la so  le *2 tra ra ket qua tra ra tich cua 2 so 
#vd a=4
#b=3
#kq=12


#vd a=4
#b=4
# kq=  ko ton tai

def chanle(a,b):
    if(a%2==0 and b%2!=0) or (a%2!=0 and b%2==0):
        if(a%2==0 and b%2!=0):
            print("kq=",(a/2)*(b*2))
        else:
            print("kq=",(a*2)*(b/2))    

    else:
        print("ko ton tai")

a=4
b=4

chanle(a,b)
        
