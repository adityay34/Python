a=float(input("Enter value 1:"))
b=float(input("Enter value 2:"))
o=input("Enter the operator(+,-,*,**,/,//,%):")
if o=="+":
    print(a+b)
elif o=="-":
    print(a-b)
else:
    if o=="*":
        print(a*b)
    elif o=="**":
        print(a**b)
    else:
        if o=="/":
            print(a/b)
        elif o=="//":
            print(a//b)
        else:
            print(a%b)