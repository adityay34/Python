a=int(input("Enter unit:"))
if a<=100:
    print("Electricity bill(in rupees):",5*a)
elif 101<=a<=200:
    print("Electricity bill(in rupees:)", (5*100+7*(a-100)))
else:
    print("Electricity bill (in rupees:)",(5*100+7*100+(a-200)*10) )
