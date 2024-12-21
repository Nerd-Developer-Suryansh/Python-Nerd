# creating a progrom of basic calculator 
b=int(input("enter 1st no: "))
c=int(input("enter 2nd no: "))
a=input("Please type in the math operation you would like to complete:\n+ for addition\n- for subtraction\n* for multiplication\n/ for division : ")

if(a=='+'):
    print("addition of",b,"amd",c,"is",b+c)
if(a=='-'):
    print("subtraction of",b,"amd",c,"is",b-c)
if(a=='*'):
    print("multiplication of",b,"amd",c,"is",b*c)    
if(a=='/'):
    print("division of",b,"amd",c,"is",b/c)
if(a!="-" and  a!="+" and a!="*"  and a!="/"):
    print("wrong input")
