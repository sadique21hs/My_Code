x=input("Enter the first number: ")
y=input("Enter the 2nd number: ")
choose=input("Choose what you want(1 is Sum, 2 is Com, 3 is Multiple, 4 is Div): ")
if int(choose)==1:
     Sum=int(x)+int(y)
     print(Sum)
elif int(choose)==2:
     Com=int(x)-int(y)
     print(Com)
elif int(choose) == 3:
     Mul=int(x)*int(y)
     print(Mul)
else:
     div=int(x)/int(y)
     print(div)



