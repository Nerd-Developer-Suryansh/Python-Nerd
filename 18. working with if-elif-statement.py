# write a progrom to find greatest digit no from  input by user
a=int(input("enter 1 no.: "))
b=int(input("enter 2 no.: "))
c=int(input("enter 3 no.: "))
if a>b and a>c:
    print("greatest no. is:",a)
elif b>a and b>c:
    print("greatest no. is:",b)
else:
    print("greatest no. is:",c)