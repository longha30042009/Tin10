## nhap so thang va so nam neu co thang do trong mam, thi hien len man hinh so ngay cua thang do neu la thang 2 cua nam nhuan
#  thi 29 ngay nam nhuan . cu 4 nam  la nam nhuan 
   #input: nhap so thang  vs so nam neu co thang do trong nam thi hien ra
    #output: neu la thang 2  cua nam nhuan la 29 ngay 
def thangnam(a,b):
    if (a<=12 and a>=1) and (b<=2025 and b>=1):
        if a==1:
            print("thang 1 co 31 ngay")
        elif  a==2:
            if b%4==0 or b==1:
                print("thang 2 la nam nhuan 29 ngay")
            else:
                print("thang 2 la nam ko nhuan 28 ngay")
        elif a==3: 
            print("thang 3 co 31 ngay") 
        elif a==4:
            print("thang 4 co  30 ngay")
        elif a==5: 
            print("thang 5 co  31 ngay")
        elif a==6:  
            print("thang 6 co 30 ngay")
        elif a==7:  
            print("thang 7 co 31 ngay") 
        elif a==8: 
            print("thang 8 co  30 ngay")
        elif a==9: 
            print("thang 9 co  31 ngay")
        elif a==10: 
            print("thang 10 co 30 ngay")
        elif a==11: 
            print("thang 11 co 31 ngay") 
        elif a==12: 
            print("thang 12 co  30 ngay")   

    else: 
       print("kh co ngay, thang, nam nao") 

    print("cuoiham")        


# a=int(input("so thang    "))
# b=int(input("so nam      "))


a=2
b=1


thangnam(a,b)


    

 