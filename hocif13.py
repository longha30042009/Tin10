#Cho 3 so tra ra ket  qua co  bao nhieu so chan co bao nhieu so le
#vd 
# a=7
#b=12
#c=10
#kq: co 2 so chan va 1 so le

#vd 
# a=8
#b=12
#c=10
#kq: co 3 so chan va 0 so le

#vd 
# a=7
#b=11
#c=10
#kq: co 1 so chan va 2 so le

#vd 
# a=7
#b=13
#c=9
#kq: co 0 so chan va 3 so le


#input:Cho 3 so tim so chan va so le

#output:
def chanle(a,b,):
      if a%2==0 and b%2==0:  
         print("co 2 so chan co 0 so le")
      elif a%2!=0 and b%2!=0:
         print("co 0 so chan co 2 so le")
      else: 
         print("co 1 so chan va 1 so le")
        


def chanle2(a,b,c):
    sochan=0
    sole=0
    if a%2==0:
        sochan=sochan+1
    else:
        sole=sole+1

    if b%2==0:
        sochan=sochan+1
    else:
        sole=sole+1
    if c%2==0:
        sochan=sochan+1
    else:
        sole=sole+1    


    print("co ",  sochan, "so chan va ", sole,"so le")    

a=10
b=100000
c=1000

chanle2(a,b,c)




