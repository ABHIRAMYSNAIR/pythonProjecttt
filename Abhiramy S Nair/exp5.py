x=int(input("enter the first number :"))
y=int(input("enter the second number :"))
z=int(input("enter the third number :"))
if(x>y)and(x>z):
    print("x is the largest number")
elif(y>x)and(y>z):
    print("y is the largest number")
else:
    print("z is the largest number")