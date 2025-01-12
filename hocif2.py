#de: cho 2 so nguyen duong a,b . Hien gia tri neu a chan va b chan  hoac a chan b le hoac a le b  chan hoac ca 2 cung le
def timchanle(a,b):
    if a>0 and b>0:
        if a%2==0 and b%2==0:
            print("a va b deu la chan") 
        elif a%2!=0 and b%2==0:
            print("a la so le, b la so chan")
        elif a%2==0 and b%2!=0:
            print("a la so chan, b la so le")
        elif a%2!=0 and b%2!=0:
            print("a la so le, b  la so  le")    


    else:
        print("a hoac b la so am")
    

    print("cuoi ham")

a = int(input('so 1  '))
b = int(input('so 2  '))

timchanle(a,b)


# lanthu 1
#a=20
#b=9
#timchanle(20,9)
#if 20>0 and 9>0 (T and T => T)
   #if 20%2==0  and 9%2==0:  (T and F => F)
   #elif 20%2!=0 and 9%2==0: (F and F => F)
   #elif 20%2==0 and 9%2!=0:(T and T =>  T)
    #print(" a la so chan, b la so le")
# print("cuoiham")

   
#lan thu 2
#a=7
#b=7
#timchanle(7,7)
#if 7>0 and 7>0 ( T  and T  => T)
    #if 7%2==0 and 7%2==0: ( F and F => F)
    # elif 7%2!=0 and 7%2==0( T and F => F)
    # elif 7%2==0 and 7%2!=0 (F and T=> F)
    # elif 7%2!=0 and 7%2!=0 (T and T => T)
    #print(" a la so le, b la so le")
#  print("cuoiham")     

#lanthu3
#a=0
#b=6
#timchanle(0,6)
#if 0>0 and 6>0(F and T =>  F)
#print(a hoav b la so am )
#  print("cuoiham") 