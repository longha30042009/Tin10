#Cho 3 so bat ki hien ra man hinh thu tu tu be den lon
#vd
#a=10
#b=20
#c=30
#kq= a<b<c


#input: cho 3 so hien len ma hinh theo thu tu tu be den lon
#output: a>b and a>c a lon nhat
#        b>a and b>c b lon nhat
#        c>a and c>b c lon nhat

def  sothutu(a,b,c):
    if a>b and a>c:
         if b<c:
              print("a>c>b")
         else:
              print("a>b>c ")
    elif b>a and b>c:
         if a<c:
              print("b>c>a")
         else:
              print("b>a>c")
    else:
         if a<b:
              print("c>b>a")
         else:
              print("c>a>b")

# a=int(input("so  "))        
# b=int(input("so  ")) 
# c=int(input("so  "))   


a=100000
b=10
c=1000000000




sothutu(a,b,c)




