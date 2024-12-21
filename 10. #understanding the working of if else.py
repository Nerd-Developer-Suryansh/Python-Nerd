#understanding the working of if else conditions in python 
# creating a program where we find greatest no between two nos.
a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))
if(a>b):
    print(a,"is a greatest no.")
elif(a<b):
    print(b,"is greatest no.")
else:
    print("wrong input")