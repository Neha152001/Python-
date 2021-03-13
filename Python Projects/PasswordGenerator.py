import itertools 
bool=False
while bool==False:
    print('Rules for password :')
    print('1.Password must be minimum of 8 characters')
    print('2.It must contain atleast one special character(@,_,$)')
    print('3.It must contain atleast one numeric character(0-9)')
    password=input('Enter password :')
    choice=input('Do u want see recomended password(y/n) :')
    if choice=='y':
        str=input("Enter some text you want in your password :")
        numeric=input("Enter some numbers you want in your password :")
        special=input('Enter the special character($,_,@) you want in your password :')
        final=str+numeric+special
        #we use iertools package to get function
        permutations=list(itertools.permutations(final))
        for i in range(5):
            print(''.join(permutations[int(i)]))
    sc=nc=int(0)
    if len(password)>=8:
        for i in password:
            if(i=='@' or i=='$' or i=='_'):
                 sc+=1;
            if(i=='0'or i=='1'or i=='2'or i=='3'or i=='4' or i=='5'or i=='6' or i=='7' or i=='8' or i=='9'):
                 nc+=1;
    if(nc!=0 and sc!=0):
        print('Valid Password')
        bool=True
    if(nc==0):
         print('Password doesnt contain numeric character')
    elif sc==0:
         print('Password doesnt contain special character')
    elif nc==0 and sc==0:
         print('Password doesnt contain numeric character and special character')
