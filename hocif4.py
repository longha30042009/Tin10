 # nhap so thang va so nam neu co thang do trong mam, thi hien len man hinh so ngay cua thang do neu la thang 2 cua nam nhuan thi 29 ngay nam nhuan  la nam la nam chan 
   #input: nhap so thang  vs so nam neu co thang do trong nam thi hien ra
    #output: neu la thang 2  cua nam nhuan la 29 ngay va nam nhuan la so chan
 
def thangnam(thang ,nam):
    if (thang<=12 and thang>=1) and (nam<=2025 and nam>=1):
        if thang==1:
           print("thang 1 co 31 ngay")

        elif thang==2:
            if nam%2==0:
                print("thang  2 nam nhuan 29 ngay")
            else:
                print("thang 2 nam ko nhuan 28 ngay")
        elif thang==3: 
            print("thang 3 co 31 ngay") 
        elif thang==4:
            print("thang 4 co  30 ngay")
        elif thang==5: 
            print("thang 5 co  31 ngay")
        elif thang==6:  
            print("thang 6 co 30 ngay")
        elif thang==7:  
            print("thang 7 co 31 ngay") 
        elif thang==8: 
            print("thang 8 co  30 ngay")
        elif thang==9: 
            print("thang 9 co  31 ngay")
        elif thang==10: 
            print("thang 10 co 30 ngay")
        elif thang==11: 
            print("thang 11 co 31 ngay") 
        elif thang==12: 
            print("thang 12 co  30 ngay")   

    else: 
       print("kh co ngay, thang, nam nao")


    print("cuoiham")
    

       

    
    


thang=int(input("so thang    "))
nam=int(input("so nam      "))

thangnam(thang,nam)


                           
               

# lan 1
# thang = 6, nam = 123
# ket qua: thang 6 co 30 ngay

# lan 2
# thang = -1, nam =  231
# ket qua= ko co ngay thang nam nao

#  lan 3
# thang =2, nam = 1
#  ket  qua = thang 2 nam ko nhuan 28 ngay


#lan 4 
# thang=2 nam =2000
#ket qua= thang 2 nam nhuan co 29 ngay


#lan 5
# thang=4 nam=2009
# ket qua= thang 4 co 30 ngay


#lan 6 
# thang= -12 nam= -2025
# ket qua= ko co ngay thang nam nao


#lan 7
# thang= 12 nam=  2025
#ket qua=  thang 12 co 30 ngay


#lan 8
# thang= -1 nam= 2026
# ket qua =  ko co ngay thang  nam nao 

