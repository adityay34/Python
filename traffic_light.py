a=str(input("Enter a color(red,green,yellow):"))
a=a.lower()
if a=="red":
    print("Stop")
elif a=="green":
    print("Go")
else:
    if a=="yellow":
        print("Wait")
    else:
        print("Invalid color")