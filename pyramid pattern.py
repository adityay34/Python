n=int(input("Enter no. of rows:"))
x=input("Enter a character:")
z=" "
for i in range(1,n+1):
    print((z*(n-i)+(2*i -1)*x))