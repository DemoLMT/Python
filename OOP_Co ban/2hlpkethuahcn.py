class hcn:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def __str__(self):
        return "Chieu dai: {0}\nChieu rong: {1}\nChu vi: {2}\nDien tich: {3}".format(self.a,self.b,self.calcPerimeter(),self.calcArea())
    def  calcPerimeter(self):
        return 2*(self.a+self.b)
    def calcArea(self):
        return self.a*self.b
class hinhlp(hcn):
    def __init__(self,a=0,b=0,h=0):
        super().__init__(a,b)
        self.h = h
    def tinh(self):
        return self.calcArea()*self.h
    def __str__(self):
        return super().__str__()+ f"\nThe tich: {self.tinh()}"
my_parallelpipe = hinhlp(3, 4, 5)
print(my_parallelpipe)