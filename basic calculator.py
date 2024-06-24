# basic calculator
a = int(input('Enter 1st number: '))#   A AND B ARE NO. ACCEPETD BY THRE USER
b = int(input('Enter 2nd number: '))


print("What type of calculation you want:\n1.addition\n2.substraction\n3.multiplication\n4.division")
x=int(input("accept your coice of calculation"))
if x==2:
   print('Sum of ',a,' and ',b, 'is ',sum(a, b))

elif x==2:
    print(' a-b is ',(a-b))
    
elif(x==3):
    print("product of",a,"and",b ,"is",(a*b))

elif(x==4):
    if(b==0):
        print("invalid")
    else:
        print(' a/b is ',(a/b))
