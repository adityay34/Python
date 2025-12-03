#it will not support construtor override,if done then will support last constructor
class car:
    def setname(self,brandname):
        self.brandname=brandname
    def getname(self):
        print(self.brandname)

    def setmodel(self,brandmodel):
    
        self.brandmodel=brandmodel
    def getmodel(self):
        print(self.brandname,self.brandmodel)
class accord(car):
    def setbrandname(self,brandname):
        self.brandname=brandname
    def getbrandname(self):
        print(self.brandname)
a=input("Enter brandname:")
b=input("Enter modelname:")
s1=accord()
s1.setname(a)
s1.setmodel(b)
s1.getname()
s1.getmodel()
