a=float(input("Enter your weight(Kg):"))
b=float(input("Enter your height(m):"))
c=a/(b**2)
decimal_places=2
if c<18.5:
    print(f"c is: {c:.{decimal_places}f} You are Underweight,please eat nutritious food.")
elif 18.5<c<24.9:
    print(f"c is: {c:.{decimal_places}f} You are Normal, keep up the good work!")
else:
    if 25<c<29.9:
        print(f"c is: {c:.{decimal_places}f} You are Overweight,keep exercising daily")
    else:
        print(f"c is: {c:.{decimal_places}f} You are Obese, you must take care of your health immediately")
      
