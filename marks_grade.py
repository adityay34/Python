a=float(input("Enter your marks:"))
if 90<=a<=100:
    print("A grade")
elif 80<=a<=89:
    print("B grade")
else:
    if 70<=a<=79:
        print('C grade')
    elif 60<=a<=69:
        print("D grade")
    else:
        print("Fail")