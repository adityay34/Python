n=int(input("Enter a number:"))
x=0
y=1
for i in range(n):
    print(x , end=' , ')
    x,y=y,x+y
    
