#Cho 2 so 1 so chac chan am va 1 so chac chan duong neu nhu am + 15 neu nhu duong -5
#vd a=-8
#b=6
#kq:  =8
#vd a=-10
#b=9
#kq=9

def amduong(a,b):
    if(a>0 and b<0)or(b>0 and a<0):
        if(a>0 and b<0):
            print("ket qua=",a-5+b+15)
        else:
              print("ket qua=",a+15+b-5)  

    else:
        print("ko co kq")  



a=-50
b=10

amduong(a,b)